import sys
import os
import re

from models import make_gemini_model, make_claude_model
from agents.router import make_router
from agents.faq import faq_answer
from agents.order import order_status


def get_model(name: str):
    if name == "gemini":
        return make_gemini_model()
    elif name == "claude":
        return make_claude_model()
    else:
        raise ValueError(f"Unsupported model: {name}")


def extract_order_id(text: str) -> str | None:
    match = re.search(r"\b\d{5}\b", text)
    return match.group(0) if match else None


if __name__ == "__main__":
    if len(sys.argv) < 1:
        name = os.path.basename(__file__)
        print(f"Usage: python {name} '<prompt>' [gemini|claude]")
        sys.exit(1)

    user_input = sys.argv[1]
    model_name = sys.argv[2] if len(sys.argv) > 2 else "gemini"

    llm = get_model(model_name)

    # ---- Route intent ----
    router = make_router(llm)
    intent = router.invoke({"input": user_input}).content.strip().lower()

    # ---- Dispatch ----
    if intent == "faq":
        result = faq_answer(user_input)

    elif intent == "order":
        order_id = extract_order_id(user_input)
        if not order_id:
            result = {"error": "Missing order ID"}
        else:
            result = order_status(order_id)

    else:
        result = {"error": f"Unknown intent: {intent}"}

    print(result)
