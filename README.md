<div align="center">
    <br>
    <!-- Logo placeholder - replace with actual logo URL later -->
    <img src="https://objectstorageapi.bja.sealos.run/73p2bjxj-images/ctxtoolkit.png" width="400" alt="Context Engineering Toolkit Logo"/>
    <br>
</div>

<div align="center">

## Context Engineering Toolkit (ctxtoolkit)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI version](https://badge.fury.io/py/ctxtoolkit.svg)](https://badge.fury.io/py/ctxtoolkit) 
[![GitHub issues](https://img.shields.io/github/issues-pr/Abossss/python-ctxtoolkit.svg)](https://GitHub.com/Abossss/python-ctxtoolkit/pull/) [![GitHub last commit](https://badgen.net/github/last-commit/Abossss/python-ctxtoolkit)](https://GitHub.com/Abossss/python-ctxtoolkit/commit/)

</div>

<div align="center">

English | <a href="README_CN.md">简体中文</a>

</div>

A practical toolkit for optimizing AI context management, helping solve problems such as content loss in long contexts, insufficient tokens, information redundancy, and context pollution.

## Core Features

### Context Builder
- Key information prioritization optimization
- Intelligent scene background integration
- Structured content layering

### Token Saver
- Automatic duplicate content merging
- Terminology compression
- Content summary generation

### Anti-Pollution System
- Error information isolation
- Term consistency checking
- Clear task boundary definition

### Tool Coordinator
- Tool boundary definition
- Dynamic call constraints
- Multi-tool collaboration workflow

## 📦 Installation

```bash
pip install ctxtoolkit
```

## 🚀 Quick Start

### 1. Context Building

```python
from ctxtoolkit import ContextBuilder

# Create context builder
builder = ContextBuilder()

# Add core instruction
builder.add_core_instruction(
    "Optimize the performance of this Python code",
    requirements=[
        "Reduce memory usage",
        "Improve execution speed",
        "Maintain original functionality"
    ]
)

# Add key information
builder.add_key_info(
    "Code functionality", "Processes 1 million user logs"
)
builder.add_key_info(
    "Current bottleneck", "Nested loops causing O(n²) complexity"
)
builder.add_key_info(
    "Available resources", "8GB RAM, 4-core CPU"
)

# Add supplementary reference
current_code = """
def process_logs(logs):
    results = []
    for i in range(len(logs)):
        for j in range(i+1, len(logs)):
            if logs[i]['user_id'] == logs[j]['user_id']:
                results.append((logs[i], logs[j]))
    return results
"""
builder.add_reference(current_code)

# Generate optimized context
optimized_context = builder.build()
print(optimized_context)
```

### 2. Token Saving Example

```python
from ctxtoolkit import TokenSaver

# Create Token saver
saver = TokenSaver()

# Define terminology
saver.add_terminology("R1", "Input format: JSON object containing name(str), age(int), tags(list[str])")
saver.add_terminology("R2", "Output format: Markdown table containing user information and tag statistics")
saver.add_terminology("R3", "Processing rules: Filter age>18, sort by number of tags descending")

# Process user data
user_data = [
    '{"name":"Zhang San","age":25,"tags":["Python","AI"]}',
    '{"name":"Li Si","age":17,"tags":["Java"]}'
]

# Generate compact context
compact_context = saver.build_compact_context(
    "Please process the following user data",
    data=user_data,
    rules=["R1", "R2", "R3"]
)
print(compact_context)
```

## 📁 Project Structure

```
ctxtoolkit/
├── ctxtoolkit/               # Core package directory
│   ├── __init__.py          # Package initialization file
│   ├── context_builder.py   # Context builder
│   ├── token_saver.py       # Token saver
│   ├── anti_pollution.py    # Anti-pollution system
│   └── tool_coordinator.py  # Tool coordinator
├── LICENSE
├── MANIFEST.in
├── README.md
└── setup.py
```

## 📚 API Documentation

API documentation has been moved to [API_DOCUMENTATION.md](API_DOCUMENTATION.md).

## 🔧 Development

### Install Development Dependencies

```bash
pip install -e .[dev]
```

### Run Tests

```bash
pytest
```

### Code Style Check

```bash
flake8
```

## 🤝 Contributing

Contributions are welcome! Feel free to submit Issues and Pull Requests.

## 📄 License

[MIT License](LICENSE)