# db.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

# Keep user data local to avoid unnecessary queries
_user_cache = {}

def get_user(phone):
    if phone in _user_cache:
        return _user_cache[phone]
    data = supabase.table("users").select("*").eq("phone", phone).execute().data
    if data:
        _user_cache[phone] = data
    return data

def create_user(phone):
    response = supabase.table("users").insert({"phone": phone, "topics": []}).execute()
    _user_cache[phone] = [{"phone": phone, "topics": []}]
    return response

def add_topic(phone, topic):
    user = get_user(phone)
    if not user:
        create_user(phone)
        topics = []
    else:
        topics = user[0]["topics"]
    if topic not in topics:
        topics.append(topic)
        supabase.table("users").update({"topics": topics}).eq("phone", phone).execute()
        _user_cache[phone][0]["topics"] = topics
    return

def remove_topic(phone, topic):
    user = get_user(phone)
    if not user:
        return
    topics = user[0]["topics"]
    if topic in topics:
        topics.remove(topic)
        supabase.table("users").update({"topics": topics}).eq("phone", phone).execute()
        _user_cache[phone][0]["topics"] = topics
    return

def list_topics(phone):
    user = get_user(phone)
    if user:
        return user[0]["topics"]
    return []

def get_all_users():
    return supabase.table("users").select("phone, topics").execute().data
