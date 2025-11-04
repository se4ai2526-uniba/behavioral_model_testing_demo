# Behavioral Model Testing Demo

This repository contains a demo of behavioral testing techniques for AI models, developed for the **Software Engineering for AI-enabled Systems** course (MSc in Computer Science, University of Bari).

Specifically, the demo showcases behavioral model testing applied to a sentiment analysis model from Hugging Face. In particular, the repository includes examples of three types of behavioral tests:

### 1. Invariance Tests (`test_invariance.py`)

Tests that verify the model's predictions remain consistent when inputs undergo transformations that should not change the sentiment (e.g., typos, punctuation changes).

### 2. Directional Tests (`test_directional.py`)

Tests that verify the model's predictions change in expected directions when inputs are modified in specific ways (e.g., adding positive/negative words should shift sentiment accordingly).

### 3. Minimum Functionality Tests (`test_minimum_functionality.py`)

Tests that verify the model can handle simple, basic cases correctly (e.g., obvious positive/negative sentences).

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

1. Install uv if you haven't already:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. Install dependencies:

    ```bash
    uv sync
    ```

## Usage

Run the tests using uv:

```bash
uv run pytest test_invariance.py
uv run pytest test_directional.py
uv run pytest test_minimum_functionality.py
```

Or run all tests at once:

```bash
uv run pytest
```
