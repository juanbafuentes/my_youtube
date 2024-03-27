"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
import my_youtube.api.yt_charts as yt_charts
import my_youtube.api.test as test
import pandas as pd

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

List = []

class State(rx.State):
    """The app state."""

#nba_data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

nba_data = yt_charts.execute_chart()

def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        rx.vstack(
            
            rx.text("Identificador de éxitos!", size="9"),
            rx.text("Por Juanba Fuentes con <3"),
            
            rx.button(
                "Ejecutar Charts",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            
            rx.box(
                rx.data_table(
                data = nba_data[["Id", "Título", "Punt", "Dias"]],
                pagination= True,
                search= True,
                sort= True,
                ),

            width="50%",
            margin="4px",  
            ),
                    
            
            align="center",
            spacing="7",
        ),
        
        height="100vh",
        
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark", accent_color="amber"
    )
)
app.add_page(index)
