# cli-helper-26

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`cli-helper-26` is a lightweight Python library designed to streamline the creation of interactive command-line interfaces. It provides intuitive abstractions for colored console output, formatted data tables, and asynchronous progress indicators with zero external dependencies.

## Features

* **Interactive Prompts**: Styled confirmation dialogs, multi-select menus, and masked password inputs out of the box.
* **Lightweight Formatting**: Render clean ASCII tables, key-value trees, and ANSI-colored text without heavy frameworks.
* **Non-blocking Spinners**: Thread-safe loading indicators and progress bars that integrate seamlessly with `asyncio` workflows.
* **Configuration Parser**: Automatic discovery and validation of JSON/YAML configuration files into typed CLI contexts.

## Installation

Install the package via `pip`:

```bash
pip install cli-helper-26
```

Or install directly from the source repository:

```bash
git clone https://github.com/Developer/cli-helper-26.git
cd cli-helper-26
pip install .
```

## Quick Start

Here is a basic example showing how to collect input and display a spinner:

```python
from cli_helper_26 import Console, Prompt, Spinner
import time

console = Console()
console.header("Deployment Script")

# Interactive prompt
environment = Prompt.choice("Select target environment", ["staging", "production"])

# Progress indicator
with Spinner("Deploying application..."):
    time.sleep(1.5)

console.success(f"Successfully deployed to {environment}!")
```

To render structured data:

```python
from cli_helper_26 import Table

table = Table(headers=["ID", "Service", "Status"])
table.add_row([1, "Auth API", "Running"])
table.add_row([2, "Database", "Healthy"])

console.render(table)
```

## License

Distributed under the MIT License. See `LICENSE` for more information.