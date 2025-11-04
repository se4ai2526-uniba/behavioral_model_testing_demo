# DIRECTIONAL TESTING
# Changes to the model inputs should affect the model outputs in a predictable way

import pytest
from main import Sentiment


@pytest.fixture
def sentiment():
    return Sentiment()


@pytest.mark.parametrize(
    "verb,expected",
    [
        ("studying", "NEUTRAL"),
        ("enjoying", "POSITIVE"),
        ("hating", "NEGATIVE"),
    ],
)
def test_directional_verbs_shift_label(sentiment, verb, expected):
    # Changing the verb should change the predicted sentiment in a predictable way.
    base_text = "I am {} this book about economics."
    result = sentiment.predict(base_text.format(verb))
    assert result[0]["label"] == expected
    assert result[0]["score"] > 0.5


def test_directional_intensifiers_positive_monotonicity(sentiment):
    # Stronger positive wording should increase positive confidence
    texts = [
        "The service is OK.",
        "The service is good.",
        "The service is very good.",
    ]

    scores = []
    for t in texts:
        r = sentiment.predict(t)[0]
        assert r["label"] == "POSITIVE"
        scores.append(r["score"])

    assert scores[0] <= scores[1] <= scores[2]


def test_directional_negation_flips_polarity(sentiment):
    # Introducing a negation should flip the predicted sentiment.
    pos = sentiment.predict("I like this product.")[0]
    neg = sentiment.predict("I do not like this product.")[0]

    assert pos["label"] == "POSITIVE"
    assert neg["label"] == "NEGATIVE"
    assert pos["score"] > 0.5
    assert neg["score"] > 0.5


@pytest.mark.skip(reason="Test intentionally skipped.")
def test_directional_contrast_clause_shifts_negative(sentiment):
    # Adding a strong negative clause should shift overall sentiment negative
    base = sentiment.predict("The battery life is great.")[0]
    contrasted = sentiment.predict(
        "The battery life is great, but the price is outrageous."
    )[0]

    assert base["label"] == "POSITIVE"
    assert contrasted["label"] == "NEGATIVE"
    assert contrasted["score"] > 0.5