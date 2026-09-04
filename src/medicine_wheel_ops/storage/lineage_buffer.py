"""
Implements cyclical file-based lineage logging.
Maintains system historical baselines using environment configuration windows.
"""

import json
import os
from typing import List, Dict, Any

class HistoricalLineageBuffer:
    """Manages version-controlled telemetry windows without unmitigated storage expansion."""

    def __init__(self, file_path: str = "src/medicine_wheel_ops/storage/lineage_history.json", max_window: int = None):
        self.file_path = file_path
        
        # Pull dynamic sliding limit boundaries from environment configurations
        if max_window is None:
            self.max_window = int(os.getenv("LINEAGE_WINDOW_MAX", 10))
        else:
            self.max_window = max_window
            
        self._initialize_buffer()

    def _initialize_log(self) -> None:
        """Internal legacy method mapping backward compatibility handles."""
        self._initialize_buffer()

    def _initialize_buffer(self) -> None:
        """Ensures the storage tracking artifact exists on disk."""
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

    def append_state(self, system_id: str, new_value: float) -> List[float]:
        """
        Appends a performance value to a system's historical tracking lineage.
        Enforces a strict sliding window threshold to prevent infinite disk bloat.
        """
        with open(self.file_path, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = {}

        system_history = history.get(system_id, [])
        system_history.append(new_value)

        # Cyclical Truncation: Enforce historical state boundary cap limits
        if len(system_history) > self.max_window:
            system_history = system_history[-self.max_window:]

        history[system_id] = system_history

        with open(self.file_path, "w") as f:
            json.dump(history, f, indent=4)

        return system_history
