import time
from datetime import datetime

# --- Times to send exercise reminders ---
exercise_times = ["09:00", "14:00", "18:00"]
sent_today = set()

# --- Print immediate reminder on startup ---
now = datetime.now()
print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] 🏃 Time to exercise! Get up and move!")

def reset_sent_reminders():
    """Clears sent reminders at midnight."""
    sent_today.clear()

# --- Continue to monitor time and send scheduled reminders ---
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    if current_time == "00:00":
        reset_sent_reminders()

    if current_time in exercise_times and current_time not in sent_today:
        print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] 🏃 Scheduled reminder: Time for exercise!")
        sent_today.add(current_time)

    time.sleep(60)
