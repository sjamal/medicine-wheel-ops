"""
Implements cyclical file-based state logging.
Maintains system ancestral memory using a strict sliding window boundary.
"""

import json
import os
from typing import List, Dict, Any

class CyclicalStateLogger:
    """Manages version-controlled telemetry windows without unmitigated storage expansion."""

    def __init__(self, file_path: str = "src/medicine_wheel_ops/storage/state_history.json", max_window: int = 10):
        self.file_path = file_path
        self.max_window = max_window
        self._initialize_log()

    def _initialize_log(self) -> None:
        """Ensures the storage tracking artifact exists on disk."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

    def append_state(self, system_id: str, new_value: float) -> List[float]:
        """
        Appends a performance value to a system's historical line tracking state.
        Enforces a strict sliding window threshold to prevent infinite disk bloat.
        """
        with open(self.file_path, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = {}

        # Fetch or initialize history for the specific system target bound
        system_history = history.get(system_id, [])
        system_history.append(new_value)

        # Cyclical Truncation: Enforce historical state boundary cap limits
        if len(system_history) > self.max_window:
            system_history = system_history[-self.max_window:]

        history[system_id] = system_history

        with open(self.file_path, "w") as f:
            json.dump(history, f, indent=4)

        return system_history
