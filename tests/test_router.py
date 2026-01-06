import time
from collections import defaultdict

from ..models import make_gemini_model, make_claude_model
from ..agents.router import make_router
from .router_cases import TEST_CASES


MODELS = {
    "gemini": make_gemini_model,
    "claude": make_claude_model,
}


def normalize(label: str) -> str:
    return label.strip().lower()


def evaluate_router(model_name, make_model):
    llm = make_model()
    router = make_router(llm)

    results = {
        "model": model_name,
        "total": len(TEST_CASES),
        "correct": 0,
        "latencies": [],
        "errors": [],
    }

    for case in TEST_CASES:
        start = time.time()
        try:
            output = router.invoke({"input": case["input"]}).content
            latency = time.time() - start
            results["latencies"].append(latency)

            if normalize(output) == case["expected"]:
                results["correct"] += 1
            else:
                results["errors"].append(
                    {
                        "input": case["input"],
                        "expected": case["expected"],
                        "got": output,
                    }
                )

        except Exception as e:
            results["errors"].append(
                {
                    "input": case["input"],
                    "error": str(e),
                }
            )

    return results


if __name__ == "__main__":
    summaries = []

    for name, factory in MODELS.items():
        result = evaluate_router(name, factory)
        summaries.append(result)

    # ---- Print results ----
    for r in summaries:
        accuracy = r["correct"] / r["total"] * 100
        avg_latency = sum(r["latencies"]) / len(r["latencies"])

        print(f"\nModel: {r['model']}")
        print(f"Accuracy: {accuracy:.1f}% ({r['correct']}/{r['total']})")
        print(f"Avg latency: {avg_latency:.2f}s")

        if r["errors"]:
            print("Errors:")
            for e in r["errors"]:
                print(f"  {e}")
