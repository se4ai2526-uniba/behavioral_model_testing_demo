import pytest

from src.main import Sentiment


@pytest.fixture(scope="session")
def sentiment():
    """Load the sentiment model once and share it across all tests."""
    return Sentiment()
