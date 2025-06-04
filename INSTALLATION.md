# Crystallizer Installation Guide

**Requirements**: Python 3.11+

Choose your preferred dependency management tool:

## 🚀 UV (Recommended - Fastest)

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install
uv venv --python 3.11
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# Or install with development dependencies
uv pip install -e ".[dev]"
```

## 📦 Poetry (Best for Development)

```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Activate shell
poetry shell

# Run with Poetry
poetry run crystallizer --help
```

## 🐍 Standard pip (Universal)

```bash
# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# For development
pip install -r requirements.txt pytest black flake8 mypy
```

## 🔧 Development Setup

If you're contributing or modifying the code:

```bash
# With UV
uv pip install -e ".[dev]"
pre-commit install

# With Poetry
poetry install --with dev
poetry run pre-commit install

# With pip
pip install -e .
pip install pre-commit
pre-commit install
```

## 🏃‍♂️ Quick Test

```bash
python crystallizer.py --help
```

You should see the crystallizer help output.

## 📋 Dependencies Explained

- **tiktoken**: OpenAI's tokenizer for accurate token counting
- **requests**: HTTP client for API calls (Ollama/OpenAI)
- **jinja2**: Template engine for system prompts
- **typing-extensions**: Enhanced type hints for Python 3.11

## 🔍 Troubleshooting

**Import Error**: Make sure you're in the activated virtual environment
**Version Issues**: Verify Python 3.11+ with `python --version`
**Network Issues**: Check firewall settings for API requests
