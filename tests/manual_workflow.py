import pprint
from dotenv import load_dotenv

from src.prompts import prompts
from src.utils import *
from src.schema import *


instructions = """
You are a helpful scientific assistant. 
Users want to explore scientific articles related to their interests. 
Your general task is to help the users to clarify and define their needs.

You have to lead the chat that yo get these information:
1. Area of interest, e.g. science category or phenomenon to create searching keywords
2. Publish date range to create search filters.
3. Optional: authors names

Start a chat with a friendly greeting. 
Chat with the user until you get this information. 
As you get them, finish the chat with the words: "Thank you for your attention. I'll search articles now".
"""

history = []
query = ""


if __name__ == "__main__":
    load_dotenv(".env")

    # -------------------------------------
    # 0 - Chat with the user
    ai_message = chat_with_llm() # starting chat with just instructions
    history.append(("ai", ai_message))
    print("\nAI:")
    pprint.pp(ai_message)
    print()

    users_message = ""

    while users_message != "FINISH":
        users_message = input("Your answer: ")
        ai_message = chat_with_llm(
            query=users_message,
            instructions=instructions,
            history=history
        )
        history.append(("human", users_message))
        history.append(("ai", ai_message))
        print("\nAI:")
        pprint.pp(ai_message)
        print()

    # -------------------------------------
    # 1 - Generate search params
    text = ""
    for message in history:
        text += f"\n\nAI Message:\n\n" if message[0] == "ai" else f"\n\nHuman Message:\n\n"
        text += message[1]

    searching_params: SearchSchema = parse_output(
        schema=SearchSchema,
        raw_text=text,
    )
    print()
    print(searching_params.keywords)
    print(searching_params.date_min)
    print(searching_params.date_max)
    print()

    # -------------------------------------
    # 2 - Find articles
    results = ArticlesMetadataLoader().load(search_params=searching_params)

    for r in results:
        presentation = chat_with_llm(
            query=prompts.article_presentation.format(
                keywords=searching_params.keywords,
                title=r.title,
                abstract=r.abstract,
                date=r.published
            )
        )
        print()
        print("-"*100)
        print(r.title)
        pprint.pp(presentation)
        print()
