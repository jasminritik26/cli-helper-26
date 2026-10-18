# cli-helper-26

`cli-helper-26` is a lightweight Python utility library designed to streamline the development of robust command-line interfaces. It provides a standardized wrapper for argument parsing, logging, and configuration management to help you build professional tools faster.

## Features

*   **Simplified Argument Mapping:** Automatically map CLI flags to typed Python dataclasses to eliminate boilerplate argument parsing code.
*   **Integrated Logger:** Pre-configured logging system that supports color-coded output levels and seamless file-writing capabilities.
*   **Auto-generated Help:** Effortlessly generate clean, formatted documentation and usage instructions based on your method annotations.
*   **Zero-Dependency Core:** Built using only Python standard libraries to ensure high portability and minimal footprint in your projects.

## Installation

Install the package via pip:

```bash
pip install cli-helper-26
```

If you are working from the source repository:

```bash
git clone https://github.com/Developer/cli-helper-26.git
cd cli-helper-26
pip install -e .
```

## Usage

Define your command logic using the `Command` decorator to automatically handle flag extraction and help menus.

```python
from cli_helper import Command, run

@Command
def process(input_file: str, verbose: bool = False):
    """Process a file with optional verbose output."""
    if verbose:
        print(f"Reading: {input_file}")
    # Application logic here
    print("Done.")

if __name__ == "__main__":
    run()
```

Run your script from the terminal:

```bash
python main.py --input_file data.csv --verbose
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.