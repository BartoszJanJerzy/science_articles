from uuid import uuid4
from dash import Dash, DiskcacheManager
from dotenv import load_dotenv
from dash_bootstrap_components.themes import SLATE, LUX, DARKLY
from dash_bootstrap_components.icons import FONT_AWESOME
from src.components import get_container_page
from src.callbacks.chat import chat_answer, add_user_message

load_dotenv(".env")


# _______________________________________________________________________
# APP
external_stylesheets = [
    LUX,
    FONT_AWESOME,
    dict(rel="preconnect", href="https://fonts.googleapis.com"),
    dict(rel="preconnect", href="https://fonts.gstatic.com"),
    dict(
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@100&family=Press+Start+2P&display=swap",
        rel="stylesheet",
    ),
]
app = Dash(
    __name__,
    title='TheHobitAlternativeHistory',
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
    prevent_initial_callbacks='initial_duplicate'
)
server = app.server


def serve_layout():
    return get_container_page()


app.layout = serve_layout


# _______________________________________________________________________
# CALLBACKS
add_user_message(app)
chat_answer(app)


if __name__ == "__main__":
    load_dotenv(".env")
    app.run(debug=True, port=1111)