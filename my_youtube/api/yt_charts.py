from pytube import Playlist
import pandas as pd
from datetime import date
from send_email import enviar_email

from utils import *

def execute_chart():

    #os.remove("resultados.html")
    baul_videos = []

    # Lista de IDs de playlists
    ids_playlists = ["PLEo57GFTc6xYGKArsqmFEbWgJk20TB_kA", "PLC9Nn_oWqVWzikYOM27pZJppBQ7p2W1lu", "PLXl9q53Jut6m55_XjigL4cjyCDoc8cTy5"]

    # Bucle para recorrer las playlists
    for id_playlist in ids_playlists:
        p = Playlist(f'https://www.youtube.com/playlist?list={id_playlist}')

        # Búcle para recorrer los vídeos de las playlist
        #for video in p.videos[:10]:
        for video in p.videos:

            un_video = {
                "Título": video.title,
                "Views": video.views,
                "Fecha": video.publish_date.strftime("%d/%m/%Y"),
                "Punt": GenerarPuntuacion(video.views,video.length,
                                            video.publish_date),
                "Dias": (date.today() - video.publish_date.date()).days,
                "Duración": video.length,
                #"Enlace": f"https://www.youtube.com/watch?v={video.video_id}"
                }
            baul_videos.append(un_video)
        # ................................................


    df = pd.DataFrame(baul_videos).sort_values(by="Punt", ascending=False)
    df.drop_duplicates(inplace=True)
    df.to_html("chart_puntuacion.html")
    enviar_email("juanbafuentes@gmail.com","Chart: Por puntuación",df.to_html())

    df = pd.DataFrame(baul_videos).sort_values(by="Dias", ascending=True)
    df.drop_duplicates(inplace=True)
    df.to_html("chart_novedades.html")
    
    enviar_email("juanbafuentes@gmail.com","Chart: Novedades",df.to_html())

    # df.to_json(force_ascii=False)
    return df.to_json(force_ascii=False)

execute_chart()
