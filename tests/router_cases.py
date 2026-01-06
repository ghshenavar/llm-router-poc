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
        "input": "I want a refund",
        "expected": "faq",
    },
    {
        "input": "How can I change my password?",
        "expected": "faq",
    },
    {
        "input": "Do you have a loyalty program?",
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
        "input": "Track my package #98765",
        "expected": "order",
    },
    {
        "input": "Has my order shipped yet?",
        "expected": "order",
    },
    {
        "input": "I received the wrong item in order 54321",
        "expected": "order",
    },
    {
        "input": "I need help with my order and a refund",
        "expected": "order",
    },
    {
        "input": "Can you tell me about shipping times?",
        "expected": "faq",
    },
    {
        "input": "Hello, I want a refund for order 11223",
        "expected": "order",
    },
    {
        "input": "Is there a warranty on this product?",
        "expected": "faq",
    },
    {
        "input": "Check order status for 44556",
        "expected": "order",
    },
]
