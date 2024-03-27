from pytube import YouTube
from datetime import date
from my_youtube.api import constantes as const
import resend
from dotenv import load_dotenv
load_dotenv()
import os


def GenerarPuntuacion(views, duracion, fecha):
  
  if duracion == 0:
    return 0
  else:
    dias_desde_publicacion = (date.today() - fecha.date()).days
    puntuacion = int(views / dias_desde_publicacion)
    return puntuacion
  
def obtener_miniatura(url_video):
    try:
        youtube = YouTube(url_video)
        miniatura = youtube.thumbnail_url
        return miniatura
    except Exception as e:
        print(f"Error al obtener la miniatura: {e}")

def descargar_video(url_video) -> bool:
    yt = YouTube(url_video)
    stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
    try:
        stream.download(const.VIDEOS_DIRECTORY)
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False


resend.api_key = os.getenv("API_RESEND")

def enviar_email(para,asunto,cuerpo):
    r = resend.Emails.send({
    "from": "onboarding@resend.dev",
    "to": para,
    "subject": asunto,
    "html": cuerpo
    })
