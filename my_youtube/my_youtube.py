"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx
import my_youtube.api.yt_charts as yt_charts
import my_youtube.api.test as test

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

List = []

class State(rx.State):
    """The app state."""



def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename)),
            
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.api.add_api_route("/chart",yt_charts.execute_chart)
app.add_page(index)
