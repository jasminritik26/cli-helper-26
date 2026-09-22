import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger("cli_helper.handler")


class CommandExecutionError(Exception):
    """Raised when CLI command processing or execution fails."""
    pass


class CLIHandler:
    """Handles argument parsing and safe command execution with edge case resilience."""

    def __init__(self, default_timeout: int = 30) -> None:
        self.default_timeout = default_timeout

    def parse_arguments(self, raw_args: Optional[List[str]]) -> Dict[str, Any]:
        """Parse raw argument lists while safely handling malformed inputs."""
        parsed: Dict[str, Any] = {"positional": [], "flags": {}}

        # Handle None or empty inputs gracefully
        if raw_args is None:
            logger.warning("Received None input for raw_args; using defaults")
            return parsed

        for item in raw_args:
            # Ignore unexpected non-string elements
            if not isinstance(item, str):
                logger.warning(f"Skipped invalid non-string argument: {item!r}")
                continue

            clean_item = item.strip()
            if not clean_item:
                continue

            if clean_item.startswith("--"):
                parts = clean_item[2:].split("=", 1)
                key = parts[0].strip().replace("-", "_")
                if not key:
                    logger.warning(f"Skipped malformed flag: {clean_item!r}")
                    continue
                val = parts[1].strip() if len(parts) > 1 else True
                parsed["flags"][key] = val
            elif clean_item.startswith("-") and len(clean_item) > 1:
                flag = clean_item[1:].strip()
                parsed["flags"][flag] = True
            else:
                parsed["positional"].append(clean_item)

        return parsed

    def execute_safely(self, command_name: str, options: Dict[str, Any]) -> int:
        """Safely run a command handling unexpected runtime failures."""
        if not command_name or not isinstance(command_name, str):
            raise CommandExecutionError("Invalid or empty command name provided")

        clean_name = command_name.strip().lower()

        try:
            flags = options.get("flags", {})
            if flags.get("debug"):
                logger.setLevel(logging.DEBUG)

            logger.info(f"Executing CLI command: {clean_name}")
            return 0
        except KeyError as err:
            logger.error(f"Missing expected option key for '{clean_name}': {err}")
            return 1
        except Exception as err:
            logger.critical(f"Unexpected error during execution of '{clean_name}': {err}")
            return 2
