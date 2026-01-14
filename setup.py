from setuptools import setup, find_packages
from pathlib import Path

# Get project root directory
HERE = Path(__file__).parent

# Read README.md as long description
with open(HERE / "README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read version information
with open(HERE / "ctxtoolkit" / "__init__.py", encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split("=")[-1].strip().strip('"')
            break

setup(
    # Package basic information
    name="ctxtoolkit",
    version=version,
    description="Context Engineering Toolkit - Practical tools for optimizing AI context management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Abossss",
    author_email="",
    url="https://github.com/Abossss/python-ctxtoolkit",  # Project URL
    project_urls={
        "Source": "https://github.com/Abossss/python-ctxtoolkit",  # Source code repository URL
        "Issues": "https://github.com/Abossss/python-ctxtoolkit/issues",  # Issue tracking URL
        "Documentation": "https://github.com/Abossss/python-ctxtoolkit/blob/main/API_DOCUMENTATION.md",  # Documentation URL
    },
    
    # Package structure
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_data={
        "ctxtoolkit": ["py.typed"],  # Mark as typed package
    },
    include_package_data=True,
    
    # Classification information
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    
    # Keywords
    keywords=[
        "ai", "context", "prompt", "llm", "tools",
        "context-engineering", "prompt-engineering", "ai-tools", "large-language-models"
    ],
    
    # Python version requirements
    python_requires=">=3.7",
    
    # Dependencies
    install_requires=[],  # No external dependencies in current version
    
    # Development dependencies
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=3.8",
            "black>=22.0",
            "isort>=5.10",
            "mypy>=0.930",
        ],
    },
    
    # Entry points (if any)
    entry_points={
        "console_scripts": [
            # For example: "context-engineering=context_engineering.cli:main",
        ],
    },
)
