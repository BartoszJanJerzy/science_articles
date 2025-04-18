from dash import Dash, html, Output, Input, State
from dash.exceptions import PreventUpdate
from src.utils import chat_with_llm



def add_user_message(app: Dash):
    @app.callback(
        [
            Output("messagesDiv", "children"),
            Output("messagesHistory", "data"),
            Output("runChatAI", "data"),
            Output("userMessage", "value"),
        ],
        Input("sendMessage", "n_clicks"),
        State("userMessage", "value"),
        State("messagesHistory", "data"),
        State("messagesDiv", "children"),
        running=[
            (Output("sendMessage", "disabled"), True, False)
        ]
    )
    def callback(
            n: int,
            user_message: str,
            history: list[tuple[str, str]],
            children: list[html.P]
    ):
        if n:
            new_message = html.P(className="humanMessage", children=html.P(user_message))
            children = [new_message] + children
            history.append(("human", user_message))
            return children, history, 1, ""
        else:
            raise PreventUpdate


def chat_answer(app: Dash):
    @app.callback(
        [
            Output("messagesDiv", "children", allow_duplicate=True),
            Output("messagesHistory", "data", allow_duplicate=True)
        ],
        Input("runChatAI", "data"),
        State("userMessage", "value"),
        State("messagesHistory", "data"),
        State("messagesDiv", "children"),
        running=[
            (Output("sendMessage", "disabled"), True, False)
        ]
    )
    def callback(
            trigger: int,
            user_message: str,
            history: list[tuple[str, str]],
            children: list[html.P]
    ):
        ai_answer = chat_with_llm(query=user_message, history=history)
        new_message = html.P(className="aiMessage", children=html.P(ai_answer))
        children = [new_message] + children
        history.append(("ai", ai_answer))
        return children, history