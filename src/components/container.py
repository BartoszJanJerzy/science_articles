from dash import html, dcc
from .chat import chat_page
from src.config import config


def get_container_page():
    return html.Div(
        id='container',
        children=[
            dcc.Store(id="messagesHistory", data=[("ai", config.initial_message)]),
            dcc.Store(id="runChatAI", data=0),
            chat_page
        ]
    )