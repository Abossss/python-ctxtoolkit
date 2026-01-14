# Changelog

## [0.1.1] - 2024-01-14

### 🐛 Bug Fixes

- Fixed PyPI upload issues
- Improved package distribution files

## [0.1.0] - 2024-01-14

### 🎉 Initial Release

ctxtoolkit is a practical toolkit for optimizing AI context management, helping solve problems such as content loss in long contexts, insufficient tokens, information redundancy, and context pollution.

### ✨ Core Features

#### 1. Context Builder
- Key information prioritization optimization
- Intelligent scene background integration
- Structured content layering
- Support for adding core instructions and requirements
- Support for key information management
- Support for supplementary reference content

#### 2. Token Saver
- Automatic duplicate content merging
- Terminology compression
- Content summary generation
- Support for terminology management
- Support for building compact contexts

#### 3. Anti-Pollution System
- Error information isolation
- Term consistency checking
- Clear task boundary definition
- Support for content verification markers
- Support for context reset

#### 4. Tool Coordinator
- Tool boundary definition
- Dynamic call constraints
- Multi-tool collaboration workflow
- Support for tool registration and availability management
- Support for workflow definition and execution

### 🛠️ Technical Features

- **Type Safety**: Complete type annotation support
- **No External Dependencies**: Lightweight design, no additional dependencies required
- **English Friendly**: Supports English documentation and error messages
- **Easy to Extend**: Modular design, easy to extend functionality
- **Test Coverage**: Comprehensive unit tests ensure functionality reliability

### 📖 Documentation

- Complete API documentation
- Detailed usage examples
- Project structure explanation

### 📦 Installation

```bash
pip install ctxtoolkit
```

### 🚀 Usage Examples

```python
# Example 1: Using ContextBuilder to build structured context
from ctxtoolkit import ContextBuilder

builder = ContextBuilder()
builder.add_core_instruction("Optimize Python code performance", requirements=["Reduce memory usage", "Improve execution speed"])
builder.add_key_info("Current bottleneck", "Nested loops causing O(n²) complexity")
context = builder.build()

# Example 2: Using TokenSaver to reduce context token consumption
from ctxtoolkit import TokenSaver

saver = TokenSaver()
saver.add_terminology("R1", "Input format: JSON object")
saver.add_terminology("R2", "Output format: Markdown table")
compact_context = saver.build_compact_context("Process data", rules=["R1", "R2"])
```

### 📄 License

MIT License
