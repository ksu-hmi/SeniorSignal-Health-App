import time
from datetime import datetime

def medication_reminder():
    # Set your medication times here (24-hour format)
    medication_times = ["09:00", "13:00", "18:00", "21:00"]

    print("Medication Reminder is running...")
    print("Times set for reminders:", ", ".join(medication_times))

    while True:
        current_time = datetime.now().strftime("%H:%M")  # Get the current time in HH:MM format

        if current_time in medication_times:
            print(f"Reminder triggered at {current_time} - Time to take your medication!")
            # Simulate a reminder message (output to the console)
            print("This is your medication reminder. Please take your medicine.")

            # Wait for a minute before checking again (prevents multiple reminders in the same minute)
            time.sleep(60)
        
        # Check every 10 seconds for the reminder time
        time.sleep(10)

if __name__ == "__main__":
    medication_reminder()

