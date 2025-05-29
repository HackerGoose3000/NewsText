from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from twilio_handler import handle_incoming_sms

app = FastAPI()

@app.post("/sms", response_class=PlainTextResponse)
async def sms_reply(
    Body: str = Form(...),
    From: str = Form(...)
):
    reply = handle_incoming_sms(From, Body)
    return reply