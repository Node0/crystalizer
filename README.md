# Crystallizer
A Map -> Reduce powerhouse,
disguised as an insight summarization tool.

Crystallizer is a programmable, LLM-powered
general purpose data traversal and transformation tool.

Its default use-case will be as insight extraction
and cohesion across N parts of long documents (think books).

However it can be programmed to do a large number
of open-ended tasks, owing to it's templated
system and task prompt design.

![Crystallizer-Web](https://github.com/user-attachments/assets/97fd2904-10e8-4fe0-96c9-4bd06a8b195e)

## Installation

**📋 [Complete Installation Guide](INSTALL.md)** - Choose your preferred tool

### Quick Links by Tool:

- **🚀 [UV Installation](INSTALL.md#-uv-recommended---fastest)** - Fastest setup
- **📦 [Poetry Installation](INSTALL.md#-poetry-best-for-development)** - Best for development  
- **🐍 [Pip Installation](INSTALL.md#-standard-pip-universal)** - Universal compatibility

### Quick Start (pip)

**Requirements**: Python 3.11+

```bash
# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Test installation
python crystallizer.py --help
```

## Usage

```bash
python crystallizer.py \
  --system-prompt system_prompt.j2 \
  --haystack-path ./chat_logs \
  --provider ollama \
  --task-label gluon_design \
  --output-dir ./crystals
```

## Configuration

Configure your LLM providers in `config.json`:

```json
{
  "providers": {
    "ollama": {
      "host": "localhost",
      "port": 11434,
      "model": "qwen2.5-coder:32b",
      "context_length": 18000
    },
    "openai": {
      "api_key": "your-api-key",
      "model": "gpt-4o-mini",
      "context_length": 128000
    }
  }
}
```

## Features

- **Token-Aware Windowing**: Automatically chunks large documents to fit LLM context limits
- **Multi-Provider Support**: Works with Ollama (local) and OpenAI (cloud) backends  
- **Template-Driven Prompts**: Jinja2 templates for custom system prompts
- **Hierarchical Processing**: 3-segment micro-windowing with merge strategies
- **Professional Logging**: Semantic progress tracking with contextual semaphores
- **Batch Processing**: Handle single files or entire directories

## License
GNU GPL v3