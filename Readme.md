# 📅 Event Scheduler System (Flask REST API)

This is a simple backend application built using Python and Flask that allows users to add, view, update, and delete events. Each event has a title, description, start time, and end time.

The API is built for use via **Postman**, and all data is persisted between sessions using a local file.

---

## ✅ Features

- Create events with title, description, start time, and end time
- View all events sorted by start time
- Update individual event details
- Delete events
- Persistent storage via JSON file
- Built-in support for Postman testing

---

📁 Project Structure

<pre> event-scheduler/ ├── app.py # Main Flask application with REST APIs ├── reminder.py # Background thread to check for upcoming events every minute ├── notifier.py # Sends email reminders using Gmail SMTP ├── utils.py # Utility functions for loading and saving events from JSON file ├── events.json # Persistent event storage (auto-created) ├── requirements.txt # Python dependencies list └── README.md # Project documentation and usage guide </pre>

---

## 🔧 Installation & Setup

1. **Clone the repository** (or download the files):
  ```bash
   git clone https://github.com/AdityaSrivastavDS/Event-Scheduler
   cd event-scheduler
  ```
2. **Install required packages**
  ```bash
  pip install requirements.txt
  ```
3. **Run the Flask server:**
  ```bash
  python app.py
  ```

## 📮 Using the API via Postman
You can interact with this API using [PostMan](https://www.postman.com/)
   
1. Create Event (POST /events)
- Method: POST

- URL: http://127.0.0.1:5000/events

- Headers:
Content-Type: application/json

- Body (raw JSON):
```bash
{
  "title": "Team Meeting",
  "description": "Discuss Q2 OKRs",
  "start_time": "2025-06-30T10:00:00",
  "end_time": "2025-06-30T11:00:00"
}
```

- Response:
```bash
{
  "message": "Event created successfully",
  "event": {
    "id": "uuid-here",
    "title": "Team Meeting",
    ...
  }
}
```

2. View All Events (GET /events)
- Method: GET

- URL: http://127.0.0.1:5000/events

- Response:
```bash
[
  {
    "id": "uuid",
    "title": "Team Meeting",
    "description": "Discuss Q2 OKRs",
    ...
  },
  ...
]
```

3. Update Event (PUT /events/<id>)
- Method: PUT

- URL: http://127.0.0.1:5000/events/<event_id>

- Headers:
Content-Type: application/json

- Body (example):
```bash
{
  "title": "Updated Meeting",
  "description": "Rescheduled with team"
}
```

- Response:
```bash
{
  "message": "Event updated successfully",
  "event": {
    "id": "uuid",
    "title": "Updated Meeting",
    ...
  }
}
```

4. Delete Event (DELETE /events/<id>)
- Method: DELETE

- URL: http://127.0.0.1:5000/events/<event_id>

- Response:
```bash
{
  "message": "Event deleted successfully"
}
```
---

## 💾 Data Persistence
All event data is stored in a local file called events.json in the project directory. Data will persist even after restarting the server.

## ✨ Optional Features (Coming Soon)
- Reminders for upcoming events

- Email notifications

- Recurring event support

- Full unit test coverage with Pytest

