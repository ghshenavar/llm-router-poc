# Set up 

The requirements are outlined in 'requirements.txt'

```
pip install -r requirements.txt
```
Before usage, `ANTHROPIC_API_KEY` for Claude and `GOOGLE_AI_KEY` for Gemini need to be set in the environment respectively.

To run the application for one specific prompt

```
python {name} '<prompt>' [gemini|claude]
```

To run the tests

```
python -m {package_name}.tests.test_route
```

The test cases can be extended/changed in `tests/router_cases.py`.

# Evaluation

The agent was tested with Claude and Gemini, as they both offer free tiers and are compatible with LangChain. After a few test, few shotting proved to be more accurate.

The models were scored based on their accuaracy and latency.

| Model   | Accuracy      | Avg Latency | Errors                                      |
|---------|--------------|------------|--------------------------------------------|
| gemini  | 93.3% (14/15)| 0.56s      | `{'input': 'I want a refund', 'expected': 'faq', 'got': 'order'}` |
| claude  | 100.0% (15/15)| 2.83s     | None                                       |


# Conclusion

While Gemini is slightly faster, the difference is negligibe for most applications. Since accuracy is typically more critical than speed for intent classification, Claude is the better choice for reliably handling FAQs and order-related queries.
