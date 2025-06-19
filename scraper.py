import requests
from bs4 import BeautifulSoup
import praw
import os

keywords = ["Vecp", "Talos", "Sonora", "Mk3", "Les George", "0620", "0630", "0920", "0301", "0302", "0303"]
sites = [
    "https://marksoutdoors.com",
    "https://www.dlttrading.com",
    "https://usamadeblade.com",
    "https://georgeknives.bigcartel.com",
    "https://lantacknives.com",
    "https://www.tacticalelements.com"
]

def keyword_in_text(text):
    return any(kw.lower() in text.lower() for kw in keywords)

def check_sites(sent_items):
    messages = []
    headers = {"User-Agent": "Mozilla/5.0"}
    for site in sites:
        try:
            response = requests.get(site, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            if "add to cart" in soup.text.lower() or "buy" in soup.text.lower():
                if keyword_in_text(soup.text):
                    if site not in sent_items:
                        messages.append(f"🛒 Можливо в наявності на {site}")
        except Exception as e:
            print(f"Error checking {site}: {e}")
    return messages

def check_reddit(sent_items):
    messages = []
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent="knife monitor by u/True-Design-6053"
    )
    subreddit = reddit.subreddit("Knife_Swap")
    for submission in subreddit.new(limit=10):
        text = submission.title + " " + submission.selftext
        if keyword_in_text(text) and submission.id not in sent_items:
           messages.append(f"🪓 Новий пост на Reddit:\n{submission.title}\n{submission.url}")
{submission.title}
message += f"New Reddit post found: {submission.title} - {submission.url}\n"

    return messages
