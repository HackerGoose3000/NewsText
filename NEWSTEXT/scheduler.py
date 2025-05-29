# scheduler.py
from db import get_all_users
from news import fetch_news, summarize_article
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))

def send_sms(phone, body):
    if len(body) > 1600:  # Cut long messages
        body = body[:1597] + "..."
    client.messages.create(
        body=body,
        from_=os.getenv("TWILIO_PHONE"),
        to=phone
    )

def run():
    articles = fetch_news()
    users = get_all_users()
    summaries = {}

    for art in articles:
        title = art["title"]
        url = art["url"]
        summaries[title.lower()] = {
            "summary": summarize_article(url) or "",
            "url": url
        }

    for user in users:
        topics = [t.lower() for t in user["topics"]]
        phone = user["phone"]
        matches = []

        for title, data in summaries.items():
            if any(t in title for t in topics):
                matches.append(f"{title.title()}\n{data['summary'][:160]}\n{data['url']}")
                if len(matches) >= 3:
                    break

        if matches:
            message = "📰 Your Briefing:\n\n" + "\n\n".join(matches)
        else:
            message = "📰 No new articles matched your interests today."

        send_sms(phone, message)
