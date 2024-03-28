import reflex as rx
import datetime
import my_youtube.constantes as const
from my_youtube.styles.styles import Size, Spacing
from my_youtube.styles.colors import Color, TextColor
#from link_bio.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.png",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
        ),
        rx.link(
            rx.box(
                f"© 2023-{datetime.date.today().year} ",
                rx.text(
                    "IdentifySong by Juanba Fuentes",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v1.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.JUANBAFUENTES_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),
                rx.text(
                    "4x4 DEVELOPER ♥ IN PROGRESS.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )


