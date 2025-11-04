# INVARIANCE TESTING
# Changes to the model inputs should not affect the model outputs

import pytest
from main import Sentiment


@pytest.fixture
def sentiment():
    return Sentiment()


@pytest.mark.parametrize(
    "token", ["service", "solution", "product", "support", "assistance", "experience"]
)
def test_invariance_positive(sentiment, token):
    text = f"I'm so happy for the excellent {token} you provide!"
    result = sentiment.predict(text)
    assert result[0]["label"] == "POSITIVE"
    assert result[0]["score"] > 0.5


@pytest.mark.parametrize(
    "token", ["service", "solution", "product", "support", "assistance", "experience"]
)
@pytest.mark.parametrize(
    "typo_text",
    [
        "I'm so hapy for the excelent {token} you provide!",
        "Im so happy for the excellent {token} you provide",
        "i'm so HAPPY for the excellent {token} you provide!!",
    ],
)
def test_invariance_positive_with_typos_and_casing(sentiment, token, typo_text):
    text = typo_text.format(token=token)
    result = sentiment.predict(text)
    assert result[0]["label"] == "POSITIVE"
    assert result[0]["score"] > 0.5


@pytest.mark.parametrize("token", ["service", "solution", "product", "support", "assistance", "experience"])
def test_invariance_negative(sentiment, token):
    text = f"I hate this {token}. It is terrible."
    result = sentiment.predict(text)
    assert result[0]["label"] == "NEGATIVE"
    assert result[0]["score"] > 0.5

@pytest.mark.parametrize(
    "token", ["service", "solution", "product", "support", "assistance", "experience"]
)
@pytest.mark.parametrize(
    "typo_text",
    [
        "I hate this {token}. It's terible.",
        "i hate this {token}. it is terrible",
        "I HATE this {token}! IT'S TERRIBLE!!",
    ],
)
def test_invariance_negative_with_typos_and_casing(sentiment, token, typo_text):
    text = typo_text.format(token=token)
    result = sentiment.predict(text)
    assert result[0]["label"] == "NEGATIVE"
    assert result[0]["score"] > 0.5


def test_invariance_neutral_robustness_to_formatting(sentiment):
    # For neutral-ish texts, don't assert a specific label; assert invariance to benign changes
    base = "The update was released yesterday."
    variants = [
        base,
        base.lower(),
        base.upper(),
        base + "  ",
        base.replace("yesterday", "yesterday."),
    ]
    base_label = sentiment.predict(base)[0]["label"]
    for text in variants:
        result = sentiment.predict(text)
        assert result[0]["label"] == base_label


def test_invariance_mixed_sentiment_consistency(sentiment):
    # Mixed sentiment: assert the label remains consistent across perturbations
    base = "The product quality is good, but the price is high."
    variants = [
        base,
        "The quality is good; however, the price is high.",
        # "Good quality product, but it's quite expensive.",
        "The product has good quality but a high price.",
    ]
    base_label = sentiment.predict(base)[0]["label"]
    for text in variants:
        result = sentiment.predict(text)
        assert result[0]["label"] == base_label
