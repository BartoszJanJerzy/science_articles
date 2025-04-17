from pydantic import BaseModel, Field


class Article(BaseModel):
    title: str
    abstract: str
    authors: list[str]
    published: str
