from transformers import pipeline


class Sentiment:
    """Encapsulates a Hugging Face sentiment analysis pipeline."""

    def __init__(self, model_name: str = "cardiffnlp/twitter-roberta-base-sentiment") -> None:
        self.classifier = pipeline("sentiment-analysis", model=model_name)

    def predict(self, texts):
        """Return sentiment predictions for a string or list of strings."""
        raw = self.classifier(texts)

        # Ensure we always work with a list of results
        results = raw if isinstance(raw, list) else [raw]

        # Some models (e.g., cardiffnlp/twitter-roberta-base-sentiment) return LABEL_0/1/2.
        # Map them to NEGATIVE/NEUTRAL/POSITIVE for test compatibility.
        label_mapping = {
            "LABEL_0": "NEGATIVE",
            "LABEL_1": "NEUTRAL",
            "LABEL_2": "POSITIVE",
        }

        normalized = []
        for item in results:
            label = item.get("label", "")
            score = item.get("score", 0.0)

            # Normalize label if it's in LABEL_*/known mapping; otherwise keep as-is
            normalized_label = label_mapping.get(label, label)

            normalized.append({
                "label": normalized_label,
                "score": score,
            })

        return normalized


def main():

    # Analyze sentiment
    texts = [
        "I love this course!",
        "This assignment is frustrating.",
        "The lecture was informative and well-structured."
    ]

    sentiment = Sentiment()
    results = sentiment.predict(texts)

    for text, result in zip(texts, results):
        print(f"Text: {text}")
        print(f"Sentiment: {result['label']}, Score: {result['score']:.3f}\n")


if __name__ == "__main__":
    main()
