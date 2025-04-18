from langchain_openai import ChatOpenAI
from src.config import config
from src.prompts import prompts
from .get_llm import get_llm


def chat_with_llm(
        instructions: str = prompts.instructions,
        query: str | None = None,
        history: list[tuple[str, str]] = None
) -> str:
    chat = get_llm()

    messages = [('system', instructions)]

    if history is not None:
        messages += history

    if query:
        messages += [('human', query)]

    return (
        chat
        .invoke(messages)
        .content
    )
