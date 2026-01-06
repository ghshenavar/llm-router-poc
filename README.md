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

# Router evaluation

The router was tested with Claude and Gemini, as they both offer free tiers and are compatible with LangChain. After some quick benchmarks, few shotting improved accuracy for both of the models so it was added to the final recipe.

In general, for routers we would prefer smaller models, since they are faster and cheaper to run. For an example of a small model, I chose to benchmark the gemini-2.0-flash, which is a smaller version of the full gemini-2.0 model (flash model is around 8B parameters).

For a comparison of the latency/accurarcy trade-off I chose to compare the small model against a full frontier model and chose the claude-sonnet-4-5, which is estimated to be in the 150B parameter range. The primary reason for this choice was to highlight the differences between a small and a large model, as opposed to such model being needed for the task at hand.

The models were scored based on their accuracy and latency.

| Model (parameters)   | Accuracy      | Avg Latency | Errors                                      |
|---------|--------------|------------|--------------------------------------------|
| gemini (8B)  | 93.3% (14/15)| 0.56s      | `{'input': 'I want a refund', 'expected': 'faq', 'got': 'order'}` |
| claude (~150B) | 100.0% (15/15)| 2.83s     | None                                       |

In our results we can see the accuracy/latency trade-off. The gemini-flash model has much smaller latency (also meaning smaller GPU time/costs), but was slightly more inaccurate in my small test data-set. The accuracy of the flash model could definelty be improved with more prompt enginerring, but the current results highlight the trade-off of using small vs large models well.

# Conclusion

While Gemini is slightly faster, the difference would probably still be acceptable in this case, but this would depend on the final agents and if the application has real-time-constraints etc. 

Since accuracy is typically more critical than speed for intent classification, Claude could be a better choice for reliably handling FAQs and order-related queries, but this is only if the added cost/latency would be acceptable for the application. 
