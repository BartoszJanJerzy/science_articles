from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import config


def get_llm():
    match config.ai_provider:
        case "openai":
            return ChatOpenAI(model=config.openai_chat_model)
        case "gemini":
            return ChatGoogleGenerativeAI(model=config.gemini_chat_model)
        case _:
            raise ValueError(f"Unknown ai provider: {config.ai_provider}")