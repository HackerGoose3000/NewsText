📬 SMS News Assistant
A lightweight Python-based personal news assistant that sends customized, real-time news updates to users via SMS. Users select topics of interest, and receive top headlines and article links powered by NewsAPI — delivered directly to their phones using Twilio.

🚀 Features
🔔 SMS-based delivery of personalized news

📑 Topic-based interest tracking

📰 Real-time headlines from NewsAPI

🧠 Scalable to thousands of users (Supabase backend)

🌐 FastAPI web server with simple endpoints

🕒 Optional scheduler for daily news delivery

📁 Project Structure
bash
Copy
Edit
sms-news-assistant/
├── main.py            # FastAPI web server
├── db.py              # Supabase user & topic functions
├── news.py            # NewsAPI logic
├── scheduler.py       # Script to send daily news to all users
├── requirements.txt   # Dependencies
└── .env               # (Not tracked) API keys and secrets
🛠️ Requirements
Python 3.8+

Twilio Account (Trial or Paid)

Supabase Account

NewsAPI Account

A verified phone number (or Twilio number)

🔐 .env File (Local Development)
Create a .env file in your root folder with the following:

env
Copy
Edit
TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth
TWILIO_PHONE=+1your_twilio_phone

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_key

NEWSAPI_KEY=your_newsapi_key
Make sure .env is in your .gitignore file.

▶️ How to Run Locally
bash
Copy
Edit
pip install -r requirements.txt
uvicorn main:app --reload
Then visit:

bash
Copy
Edit
http://localhost:8000/subscribe?phone=+1234567890&topics=tech,space
⏰ Run the Scheduler (Manual or Cron)
To send news to all users manually:

bash
Copy
Edit
python scheduler.py
Or run on a schedule using a cron job or Render's free cron service.

🌐 Deployment (Free with Render)
Push this repo to GitHub

Connect to Render

Add your .env values in the "Environment Variables" section

Use this start command:

bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 10000
📦 Future Features
Stripe integration for paid tiers

Web-based user dashboard

AI summarization of news

SMS replies to change preferences

🧠 Built With
FastAPI

Twilio

Supabase

NewsAPI

Uvicorn

