import os
import time
import logging
from telegram import Bot
from scraper import check_sites, check_reddit

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
bot = Bot(token=TELEGRAM_TOKEN)

logging.basicConfig(level=logging.INFO)

sent_items = set()

def send_telegram_message(message):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def main_loop():
    global sent_items
    while True:
        logging.info("Checking websites...")
        new_items = check_sites(sent_items)
        for item in new_items:
            send_telegram_message(item)
            sent_items.add(item)

        logging.info("Checking Reddit...")
        reddit_items = check_reddit(sent_items)
        for item in reddit_items:
            send_telegram_message(item)
            sent_items.add(item)

        time.sleep(60)

if __name__ == "__main__":
    main_loop()