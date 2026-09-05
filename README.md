# cli-helper-26

`cli-helper-26` is a lightweight Python toolkit designed to streamline command-line interface development by automating repetitive boilerplate tasks. It provides a robust abstraction layer for handling subcommands, configuration parsing, and terminal formatting with minimal code.

## Features

*   **Subcommand Auto-Routing:** Automatically maps command-line arguments to function signatures, removing the need for complex `argparse` nesting.
*   **Built-in Config Manager:** Seamlessly integrates with YAML and JSON files to load local tool settings or user preferences.
*   **Styled Output API:** Includes helper methods for consistent logging, progress bars, and color-coded status messages compatible with all standard terminals.
*   **Zero-Dependency Core:** Built using only Python standard libraries to ensure portability and high performance across environments.

## Installation

Install the package directly from PyPI using `pip`:

```bash
pip install cli-helper-26
```

Alternatively, for development installation, clone the repository:

```bash
git clone https://github.com/Developer/cli-helper-26.git
cd cli-helper-26
pip install -e .
```

## Basic Usage

Initialize your CLI app by inheriting from the `BaseCLI` class to enable automatic command registration:

```python
from cli_helper import BaseCLI

class MyTool(BaseCLI):
    def run_greet(self, name: str = "World"):
        """Greet a user."""
        self.logger.info(f"Hello, {name}!")

if __name__ == "__main__":
    MyTool().run()
```

Run your new CLI tool from the terminal:

```bash
python main.py greet --name "Developer"
# Output: [INFO] Hello, Developer!
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.