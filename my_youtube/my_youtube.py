"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
import my_youtube.api.yt_charts as yt_charts
import my_youtube.api.test as test
import pandas as pd

from my_youtube import constantes as const
from my_youtube.styles.styles import Size, Spacing
from my_youtube.styles.colors import Color, TextColor
from my_youtube.components.footer import footer
from my_youtube.components.navbar import navbar
from my_youtube.state.PageState import PageState

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"
charts_directory = const.CHARTS_DIRECTORY

class State(rx.State):
    """The app state."""
    
    data_videos = []
    print(f"{charts_directory}chart_puntuacion.csv")
    data_videos = pd.read_csv(f"{charts_directory}chart_puntuacion.csv")
    
    # @rx.var
    # def traer_videos(self) -> pd.DataFrame:
    #     yt_charts.execute_chart("PLEo57GFTc6xYGKArsqmFEbWgJk20TB_kA")
    #     #data_videos = pd.read_csv(f"{charts_directory}chart_puntuacion.csv")
    #     #print(data_videos)

@rx.page(
   #on_load=State.traer_videos()
)

def index() -> rx.Component:
    return rx.box(
        #rx.theme_panel(),
        navbar(),

        rx.center(
            rx.vstack(
                rx.text("¡IdentifySong!", size="9"),
                rx.text("By Juanba Fuentes"),
                rx.button(
                    "Ejecutar Charts",
                    on_click=lambda: rx.redirect(docs_url),
                    size="4",
                ),
                
                rx.box(
                    rx.vstack(
                        rx.heading("Listado de éxitos en Youtube"),
                        
                        rx.data_table(
                        data = State.data_videos[["Id", "Título"]],
                        pagination= True,
                        #search= True,
                        sort= True,
                        ),
                    ),
                width="70%",
                margin="5px"  
                ),
            
            footer(),

            margin_top=Size.VERY_BIG.value,
            align="center",
            spacing="7",
            ),

        height="100vh",
        ),

        

    bg=Color.BACKGROUND.value,
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", accent_color="amber"
    )
)
app.add_page(index)
