# MINIMUM FUNCTIONALITY TESTING
# Simple combinations of inputs and expected outputs

import pytest
from main import Sentiment


@pytest.fixture
def sentiment():
    return Sentiment()


@pytest.mark.parametrize(
    "word,expected",
    [
        ("Hope", "POSITIVE"),
        ("Despair", "NEGATIVE"),
        ("Eggs", "NEUTRAL"),
    ],
)
def test_minimum_functionality(sentiment, word, expected):
    text = f"{word} is all we have left."
    result = sentiment.predict(text)
    assert result[0]["label"] == expected
    assert result[0]["score"] > 0.5


@pytest.mark.parametrize(
    "text,expected",
    [
        ("I absolutely love this movie!", "POSITIVE"),
        ("This is the worst experience I've ever had.", "NEGATIVE"),
        ("I'm thrilled with the results.", "POSITIVE"),
        ("I hate everything about this.", "NEGATIVE"),
        ("It is a chair.", "NEUTRAL"),
        ("Fantastic job, well done!", "POSITIVE"),
        ("This tastes awful.", "NEGATIVE"),
        ("Water boils at 100 degrees Celsius.", "NEUTRAL"),
    ],
)
def test_minimum_functionality_sentences(sentiment, text, expected):
    result = sentiment.predict(text)
    assert result[0]["label"] == expected
    assert result[0]["score"] > 0.5

