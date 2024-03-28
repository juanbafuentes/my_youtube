import reflex as rx
import datetime
from my_youtube.styles.styles import Size, Spacing
from my_youtube.styles.colors import Color, TextColor

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.image(src="/logo.png", width="50px"),
                rx.heading("IdentifySong", size="8"),
                rx.flex(
                    rx.badge(f"© 2023-{datetime.date.today().year}"),
                ),
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Menu", color=Color.PRIMARY.value, size="3", radius="medium", px=4, py=2),
                ),
                rx.menu.content(
                    rx.menu.item("Graph"),
                    rx.menu.separator(),
                    rx.menu.item(
                        rx.link(
                            rx.hstack(rx.text("20Dataset"), rx.icon(tag="download")),
                            href="https://media.geeksforgeeks.org/wp-content/uploads/nba.csv",
                        ),
                    ),
                ),
            ),
            justify="between",
            border_bottom=Color.PRIMARY.value,
            padding_inline_start="2em",
            padding_inline_end="2em",
            padding_top="1em",
            padding_bottom="1em",
            bg=Color.BLACK.value,
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )