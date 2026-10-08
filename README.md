# cli-helper-26

`cli-helper-26` is a lightweight Python utility library designed to streamline the development of command-line interfaces. It provides an abstraction layer over `argparse` and `click`, enabling developers to build robust, user-friendly terminal tools with minimal boilerplate.

## Features

*   **Smart Argument Parsing:** Automatically generates type-safe flag handling and intuitive help menus with minimal configuration.
*   **Built-in Color Support:** Integrated formatting utilities to output stylized ANSI text and warning banners to the console.
*   **Cross-Platform Path Resolution:** Simplifies complex file system operations and cross-OS configuration directory management.
*   **Execution Hooks:** Simple decorators for setting up pre-command validation and logging without polluting your main business logic.

## Installation

Ensure you have Python 3.8+ installed. You can install the package directly from PyPI:

```bash
pip install cli-helper-26
```

If you are contributing to the source code, install in editable mode:

```bash
git clone https://github.com/Developer/cli-helper-26.git
cd cli-helper-26
pip install -e .
```

## Basic Usage

Getting started is as simple as decorating your command function. Below is an example of creating a tool that accepts a mandatory path argument:

```python
from cli_helper import Command, printer

app = Command(name="file-tool", version="1.0.0")

@app.command(help="Print the absolute path of a file")
def resolve(path: str):
    import os
    abs_path = os.path.abspath(path)
    printer.success(f"Resolved path: {abs_path}")

if __name__ == "__main__":
    app.run()
```

Run the script from your terminal:

```bash
python main.py resolve ./my_file.txt
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.