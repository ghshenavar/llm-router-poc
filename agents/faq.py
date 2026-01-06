def faq_answer(query: str) -> str:
    qanda = {
        "What is your return policy?": "You can return any item within 30 days of purchase.",
        "Do you offer international shipping?": "Yes, we ship to most countries worldwide.",
        "How can I track my order?": "You can track your order using the tracking link sent to your email.",
    }
    return qanda.get(query, "This is a dummy answer to the FAQ.")
