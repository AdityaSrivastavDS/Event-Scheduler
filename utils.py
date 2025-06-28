import json
import os

# File path for saving events
EVENT_FILE = 'events.json'

# Load events from file
def load_events():
    if not os.path.exists(EVENT_FILE):
        return []
    try:
        with open(EVENT_FILE, 'r') as file:
            content = file.read().strip()
            if not content:  # File is empty
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # If JSON is invalid, return empty list and log error
        print(f"Warning: Invalid JSON in {EVENT_FILE}, returning empty list")
        return []

# Save events to file
def save_events(events):
    with open(EVENT_FILE, 'w') as file:
        json.dump(events, file, indent=4)
