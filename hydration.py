import time

def hydration_reminder():
    print("💧 Reminder: It's time to drink some water!")

def start_hydration_reminders(interval_minutes):
    print("Water reminder started. You will be reminded every", interval_minutes, "minutes.")
    while True:
        time.sleep(interval_minutes * 60)
        hydration_reminder()

# Set the reminder interval in minutes
reminder_interval = 60  # Change this to whatever you like

# Start the reminder loop
start_hydration_reminders(reminder_interval)

