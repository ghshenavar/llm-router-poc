TEST_CASES = [
    {
        "input": "What is your return policy?",
        "expected": "faq",
    },
    {
        "input": "Do you ship internationally?",
        "expected": "faq",
    },
    {
        "input": "Where is my order 12345?",
        "expected": "order",
    },
    {
        "input": "Order 67890 status please",
        "expected": "order",
    },
    {
        "input": "I want a refund",
        "expected": "faq",
    },
]
