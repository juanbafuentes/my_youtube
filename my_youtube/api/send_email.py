import resend
from dotenv import load_dotenv
load_dotenv()
import os

resend.api_key = os.getenv("API_RESEND")

def enviar_email(para,asunto,cuerpo):
    r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": para,
    "subject": asunto,
    "html": cuerpo
    })
