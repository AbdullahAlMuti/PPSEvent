import time
import schedule
from datetime import datetime, timedelta
from telegram import Bot

# Your bot token and chat ID
TOKEN = "7987213945:AAFmc4wzS8B4EZvGjRCgW6BJKWkVxG9Oo0I"
CHAT_ID = "@PPSUSABot"  # Group or user chat ID

# List of upcoming events (add more as needed)
EVENTS = [
    {"name": "Super Bowl", "date": "2025-02-09"},
    {"name": "Valentine’s Day", "date": "2025-02-14"},
    {"name": "Easter", "date": "2025-04-20"},
    {"name": "Mother’s Day", "date": "2025-05-11"},
    {"name": "Black Friday", "date": "2025-11-28"},
    {"name": "Christmas", "date": "2025-12-25"},
    # Add more events here...
]

# Initialize the bot
bot = Bot(token=TOKEN)

# Function to send reminder 10 days before the event
def send_reminder(event_name, event_date):
    today = datetime.today().date()
    event_date = datetime.strptime(event_date, "%Y-%m-%d").date()
    days_left = (event_date - today).days

    if days_left == 10:
        message = f"📢 Reminder: {event_name} is in 10 days! 🛒 Plan your listings now!"
        bot.send_message(chat_id=CHAT_ID, text=message)

# Schedule notifications for each event
def schedule_notifications():
    for event in EVENTS:
        schedule.every().day.at("09:00").do(send_reminder, event["name"], event["date"])

def main():
    # Set up scheduled reminders
    schedule_notifications()
    print("🔔 Event Reminder Bot is running...")

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    main()
