import reflex as rx
import my_youtube.api.yt_charts as yt_charts
from my_youtube.state.PageState import PageState 

def table() -> rx.Component:
         return rx.data_table(
                data = PageState.traer_videos[["Id", "Título", "Punt", "Dias"]],
                pagination= True,
                search= True,
                sort= True,
                )