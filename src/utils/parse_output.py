from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from src.prompts import prompts
from .get_llm import get_llm


def parse_output(
        raw_text: str,
        schema: BaseModel,
        prompt: str = prompts.parse_response
) -> BaseModel:
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=schema)
    prompt = PromptTemplate(
        template=prompt,
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    chain = prompt | llm | parser
    answer = chain.invoke({"text": raw_text})
    return answer
