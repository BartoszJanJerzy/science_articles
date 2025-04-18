from pydantic import BaseModel, Field
from typing import Literal


class Article(BaseModel):
    title: str
    abstract: str
    authors: list[str]
    published: str


class SearchKeyword(BaseModel):
    """A schema for a single searching keyword"""
    value: str = Field(description="A searching keyword -  a short phrase containing 1 or 2 words")
    category: Literal["ti", "au", "abs", "cat", "all"] = Field(description="A place where the keyword should appear")


class SearchSchema(BaseModel):
    """This is schema for searching params"""

    keywords: list[SearchKeyword] = Field(
        description="A list of searching keywords. Min 1 and max 3",
        min_length=1,
        max_length=3
    )
    date_min: str = Field(
        description="A minimum date value in the following format: YYYYMMDD, e.g. 20200101",
        default="20200101"
    )
    date_max: str | None = Field(
        description="A maximum date value in the following format: YYYYMMDD, e.g. 20200101. "
                    "Leave None if its not provided",
        default=None
    )