# Behavioral Model Testing Demo

This repository contains a demo of behavioral testing techniques for AI models, developed for the **Software Engineering for AI-enabled Systems** course (MSc in Computer Science, University of Bari).

Specifically, the demo showcases behavioral model testing applied to a sentiment analysis model from Hugging Face. In particular, the repository includes examples of three types of behavioral tests:

### 1. Invariance Tests (`tests/test_invariance.py`)

Tests that verify the model's predictions remain consistent when inputs undergo transformations that should not change the sentiment (e.g., typos, punctuation changes).

### 2. Directional Tests (`tests/test_directional.py`)

Tests that verify the model's predictions change in expected directions when inputs are modified in specific ways (e.g., adding positive/negative words should shift sentiment accordingly).

### 3. Minimum Functionality Tests (`tests/test_minimum_functionality.py`)

Tests that verify the model can handle simple, basic cases correctly (e.g., obvious positive/negative sentences).

## Project Structure

```txt
├── src/                                # Source code package
│   ├── __init__.py                     # Package initialization
│   ├── main.py                         # Main sentiment analysis model
│   └── utilities.py                    # Utility functions (e.g., text preprocessing)
├── tests/                              # Test package
│   ├── __init__.py                     # Test package initialization
│   ├── test_directional.py             # Directional behavioral tests
│   ├── test_invariance.py              # Invariance behavioral tests
│   ├── test_minimum_functionality.py   # Minimum functionality tests
│   └── test_utilities.py               # Standard tests for utility functions
├── pyproject.toml                      # Project configuration and dependencies
└── README.md                           # This file
```

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

## VSCode Setup

After running `uv sync`, the VSCode pytest extension should automatically detect the tests. If it doesn't:

1. Reload VSCode window (Cmd+Shift+P -> "Developer: Reload Window")
2. Make sure the Python interpreter is set to `.venv/bin/python`
3. The `.vscode/settings.json` file configures pytest for this project

## Usage

### Running Tests

Run all tests using uv:

```bash
uv run pytest
```

Or run specific test files:

```bash
uv run pytest tests/test_invariance.py
uv run pytest tests/test_directional.py
uv run pytest tests/test_minimum_functionality.py
uv run pytest tests/test_utilities.py
```

### Running the Main Script

Execute the sentiment analysis demo:

```bash
uv run python -m src.main
```
