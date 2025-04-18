import dash_bootstrap_components as dbc
from dash import html
from src.config import config


chat_page = html.Div(
    id='chatPage',
    className="page",
    children=[
        html.H2("Discuss your scientific interest"),
        html.Div(
            id="messagesDiv",
            children=[html.P(className="aiMessage", children=html.P(config.initial_message))]
        ),
        dbc.Input(
            id='userMessage',
            placeholder="Your answer here ...",
            type='text'
        ),
        dbc.Button(
            id="sendMessage",
            color="success",
            children=["Send"]
        )
    ]
)