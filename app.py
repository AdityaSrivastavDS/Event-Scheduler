from flask import Flask, request, jsonify
from datetime import datetime
import uuid
from utils import load_events, save_events
from reminder import start_reminder_thread

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <h2>🎯 Event Scheduler API</h2>
    <p>This is a backend service. Use <strong>Postman</strong> to interact with:</p>
    <ul>
        <li><code>GET /events</code> → List events</li>
        <li><code>POST /events</code> → Create an event</li>
        <li><code>PUT /events/&lt;id&gt;</code> → Edit an event</li>
        <li><code>DELETE /events/&lt;id&gt;</code> → Delete an event</li>
    </ul>
    <p>📫 Reminder emails will be sent automatically if events are due within 1 hour.</p>
    '''



# Get all events sorted by start time
@app.route('/events', methods=['GET'])
def get_events():
    events = load_events()
    events.sort(key=lambda e: e['start_time'])
    return jsonify(events), 200

# Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()

    # Validate required fields
    for field in ['title', 'description', 'start_time', 'end_time']:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400

    try:
        start_time = datetime.fromisoformat(data['start_time'])
        end_time = datetime.fromisoformat(data['end_time'])
    except ValueError:
        return jsonify({'error': 'Invalid datetime format (use ISO format)'}), 400

    if start_time >= end_time:
        return jsonify({'error': 'Start time must be before end time'}), 400

    event = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'description': data['description'],
        'start_time': data['start_time'],
        'end_time': data['end_time']
    }

    events = load_events()
    events.append(event)
    save_events(events)

    return jsonify({'message': 'Event created successfully', 'event': event}), 201

# Update an existing event
@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    events = load_events()
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Validate datetime fields if they are being updated
    if 'start_time' in data or 'end_time' in data:
        try:
            if 'start_time' in data:
                datetime.fromisoformat(data['start_time'])
            if 'end_time' in data:
                datetime.fromisoformat(data['end_time'])
        except ValueError:
            return jsonify({'error': 'Invalid datetime format (use ISO format)'}), 400
    
    updated = False
    for event in events:
        if event['id'] == event_id:
            # Update only the provided fields
            for key in ['title', 'description', 'start_time', 'end_time']:
                if key in data:
                    event[key] = data[key]
            updated = True
            break

    if not updated:
        return jsonify({'error': 'Event not found'}), 404

    save_events(events)
    return jsonify({'message': 'Event updated successfully'}), 200

# Delete an event
@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    updated_events = [event for event in events if event['id'] != event_id]

    if len(events) == len(updated_events):
        return jsonify({'error': 'Event not found'}), 404

    save_events(updated_events)
    return jsonify({'message': 'Event deleted successfully'}), 200

if __name__ == '__main__':
    start_reminder_thread()  # Launch background reminder thread
    app.run(debug=True)
