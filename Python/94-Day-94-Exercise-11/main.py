import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(title="Drink Water Now!",
                        message="It's time to drink water. Stay hydrated!",
                        app_name="Water Reminder",
                        timeout=10)
    time.sleep(60 * 60)  # Remind every hour
