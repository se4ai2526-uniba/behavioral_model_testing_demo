from transformers import pipeline


class Sentiment:
    """Encapsulates a Hugging Face sentiment analysis pipeline."""

    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english") -> None:
        self.classifier = pipeline("sentiment-analysis", model=model_name)

    def predict(self, texts):
        """Return sentiment predictions for a string or list of strings."""
        return self.classifier(texts)


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
