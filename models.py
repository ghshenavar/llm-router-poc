from langchain.chat_models import BaseChatModel


def make_gemini_model() -> BaseChatModel:
    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=1.0,
    )


def make_claude_model() -> BaseChatModel:
    from langchain_anthropic import ChatAnthropic

    return ChatAnthropic(
        model="claude-sonnet-4-5-20250929",
        temperature=1.0,
    )
