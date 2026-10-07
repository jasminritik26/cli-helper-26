import os
import sys
from typing import List, Optional

class CLIHandler:
    def __init__(self, workspace: str = "."):
        self.workspace = workspace
        self.files = []

    def scan_directory(self) -> List[str]:
        """Collects all python files in the target directory."""
        self.files = [
            f for f in os.listdir(self.workspace) 
            if f.endswith(".py")
        ]
        return self.files

    def cleanup_empty_files(self) -> int:
        """Removes empty python files from the workspace."""
        removed_count = 0
        for filename in self.files:
            path = os.path.join(self.workspace, filename)
            if os.path.getsize(path) == 0:
                os.remove(path)
                removed_count += 1
        return removed_count

    def run(self) -> None:
        """Orchestrates scan and cleanup operations."""
        try:
            self.scan_directory()
            count = self.cleanup_empty_files()
            print(f"Successfully removed {count} empty files.")
        except OSError as e:
            print(f"System error during cleanup: {e}", file=sys.stderr)

if __name__ == "__main__":
    manager = CLIHandler()
    manager.run()