from pytube import YouTube
from datetime import date

def GenerarPuntuacion(views, duracion, fecha):
  
  if duracion == 0:
    return 0
  else:
    dias_desde_publicacion = (date.today() - fecha.date()).days
    puntuacion = int(views / dias_desde_publicacion)
    return puntuacion