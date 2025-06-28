import threading
import time
from datetime import datetime, timedelta
from utils import load_events
from notifier import send_email  # We'll define this next

# Check for events within the next hour
def check_reminders():
    while True:
        now = datetime.now()
        upcoming = []

        # Load events from file
        events = load_events()

        for event in events:
            event_time = datetime.fromisoformat(event['start_time'])

            # Event is within the next hour
            if now <= event_time <= now + timedelta(hours=1):
                upcoming.append(event)

        for event in upcoming:
            print(f"\n🔔 Reminder: Upcoming event '{event['title']}' at {event['start_time']}")
            send_email(event)  # Send email reminder

        time.sleep(60)  # Check every minute

# Start reminders in a separate background thread
def start_reminder_thread():
    thread = threading.Thread(target=check_reminders, daemon=True)
    thread.start()
