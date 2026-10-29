# cli-helper-26

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

`cli-helper-26` is a lightweight Python utility designed to streamline command-line tool development with automatic argument parsing and rich terminal formatting. It enables developers to create polished interactive prompts, progress indicators, and structured table views with minimal boilerplate code.

## Features

* **Declarative Command Routing**: Use Python decorators to register subcommands, automatic type validation, and generated help menus instantly.
* **Rich Output Formatting**: Built-in support for ANSI color styling, dynamic progress bars, and auto-aligned tabular data rendering.
* **Interactive Prompts**: Ready-to-use input handlers for fuzzy select lists, hidden secret inputs, and multi-choice confirmation dialogs.
* **Async Task Spinners**: Non-blocking loading spinners to provide visual feedback during background I/O operations.

## Installation

Install the package directly from PyPI:

```bash
pip install cli-helper-26
```

Or install the latest development build from source:

```bash
git clone https://github.com/Developer/cli-helper-26.git
cd cli-helper-26
pip install .
```

## Quick Start

Create an interactive CLI application in just a few lines of Python:

```python
from cli_helper_26 import CLIApp, Table, spinner

app = CLIApp(name="System Monitor", version="1.0.0")

@app.command()
def inspect(target: str, detailed: bool = False):
    """Inspect system resource allocation for a given service."""
    with spinner(f"Analyzing metrics for {target}..."):
        # Simulated workload
        records = [("CPU Usage", "12.4%"), ("Memory", "256MB")]

    table = Table(headers=["Metric", "Value"])
    for metric, value in records:
        table.add_row(metric, value)
    
    table.render()

if __name__ == "__main__":
    app.run()
```

Run the command directly from your terminal:

```bash
python app.py inspect --target "DatabaseService" --detailed
```

## License

Distributed under the MIT License. See `LICENSE` for more information.