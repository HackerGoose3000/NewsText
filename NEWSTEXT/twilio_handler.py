from db import add_topic, remove_topic, list_topics

def handle_incoming_sms(phone: str, message: str) -> str:
    msg = message.strip().lower()

    if msg.startswith("add "):
        topic = msg[4:].strip()
        add_topic(phone, topic)
        return f"✅ Topic '{topic}' added."

    elif msg.startswith("remove "):
        topic = msg[7:].strip()
        remove_topic(phone, topic)
        return f"❌ Topic '{topic}' removed."

    elif msg == "list":
        topics = list_topics(phone)
        return f"📋 Your topics: {', '.join(topics)}"

    elif msg == "stop":
        return "👋 You’ve been unsubscribed (feature coming soon)."

    else:
        return "❓ Use ADD <topic>, REMOVE <topic>, LIST, or STOP."
