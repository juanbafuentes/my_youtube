from pytube import Playlist
import pandas as pd
from datetime import date
import os
import my_youtube.constantes as const
import my_youtube.utils as utils


def execute_chart(id_playlist: str) -> pd.DataFrame:

    charts_directory = const.CHARTS_DIRECTORY
    #if os.path.exists(f"{charts_directory}chart_puntuacion.csv"):os.remove(f"{charts_directory}chart_puntuacion.csv")
    #if os.path.exists(f"{charts_directory}chart_puntuacion.html"):os.remove(f"{charts_directory}chart_puntuacion.html")
        
    baul_videos = []

    # Lista de IDs de playlists
    # ids_playlists = ["PLEo57GFTc6xYGKArsqmFEbWgJk20TB_kA",
    #                  "PLC9Nn_oWqVWzikYOM27pZJppBQ7p2W1lu",
    #                  "PLXl9q53Jut6m55_XjigL4cjyCDoc8cTy5"]
    
    p = Playlist(f'https://www.youtube.com/playlist?list={id_playlist}')

    for video in p.videos[:5]:

        un_video = {
            "Id": video.video_id,
            "Título": video.title,
            "Artist": video.author,
            "Views": video.views,
            "Fecha": video.publish_date.strftime("%d/%m/%Y"),
            "Punt": utils.GenerarPuntuacion(video.views,
                                      video.length,
                                      video.publish_date),
            "Dias": (date.today() - video.publish_date.date()).days,
            "Enlace": f"https://www.youtube.com/watch?v={video.video_id}"
            }
        
        #descargar_video(f"https://www.youtube.com/watch?v={video.video_id}")

        baul_videos.append(un_video)
        # ................................................






    df = pd.DataFrame(baul_videos)\
            .sort_values(by="Punt", ascending=False)\
            .head(5)
    df.drop_duplicates(inplace=True)

    df.to_html(f"{charts_directory}chart_puntuacion.html",\
                render_links=True,\
                classes='table table-stripped',
                index=False)
    
    df.to_csv(f"{charts_directory}chart_puntuacion.csv",\
               encoding='utf-8')
    
    # enviar_email("juanbafuentes@gmail.com","Chart: Por puntuación",df.to_html())
    
    # df = pd.DataFrame(baul_videos)\
    #     .sort_values(by="Dias", ascending=True)\
    #     .head(5)
    
    # df.drop_duplicates(inplace=True)
    # df.to_html(f"{charts_directory}chart_novedades.html",\
    #            classes='table table-stripped',\
    #            render_links=True)
    
    # enviar_email("juanbafuentes@gmail.com","Chart: Novedades",df.to_html())
    # df.to_json(force_ascii=False)
    return (df)

execute_chart("PLEo57GFTc6xYGKArsqmFEbWgJk20TB_kA")

