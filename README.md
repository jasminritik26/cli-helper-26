# cli-helper-26

`cli-helper-26` is a lightweight Python utility library designed to streamline the development of robust command-line interfaces. It provides a set of wrappers to handle argument parsing, colorful logging, and terminal formatting with minimal boilerplate.

## Features

*   **Smart Argument Validation**: Built-in decorators to enforce type checking and range constraints on CLI arguments.
*   **Intuitive Logging**: Pre-configured handlers for standardized STDOUT/STDERR output with automatic ANSI color support.
*   **Configuration Persistence**: Automatic JSON-based session saving to cache user preferences between executions.
*   **Zero-Dependency Core**: Developed with pure Python to ensure high compatibility and minimal bloat in containerized environments.

## Installation

Install the package via pip:

```bash
pip install cli-helper-26
```

If you are developing locally, clone the repository and install in editable mode:

```bash
git clone https://github.com/Developer/cli-helper-26.git
cd cli-helper-26
pip install -e .
```

## Basic Usage

Integrate `cli-helper-26` into your project to handle complex CLI flows effortlessly:

```python
from cli_helper import CommandManager, Logger

# Initialize the manager
cli = CommandManager(name="my-tool")
log = Logger()

@cli.command("greet")
def greet(name: str):
    """Greets the user."""
    log.info(f"Hello, {name}!")

if __name__ == "__main__":
    cli.run()
```

Run your script from the terminal:

```bash
python main.py greet --name "Developer"
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.