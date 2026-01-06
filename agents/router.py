from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import BaseChatModel


def make_router(model: BaseChatModel):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """Classify the user's intent into one of "faq" or "order".

                Examples:
                User: What is your return policy? → faq
                User: Where is my order 12345? → order
                User: Do you ship internationally? → faq
                User: Order 67890 status → order

                Return only faq or order.""",
            ),
            ("human", "{input}"),
        ]
    )

    return prompt | model
