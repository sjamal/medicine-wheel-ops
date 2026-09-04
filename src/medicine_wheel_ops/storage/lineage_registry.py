"""
Data persistence registry tracking system architectural lineage and historical profiles.
Establishes relational dependency mapping layers across system nodes.
"""

import json
import os
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field

class SystemProfile(BaseModel):
    """Schema boundary defining place-based system lineage and relational network links."""
    system_id: str
    historical_baseline_years: int
    criticality_tier: int
    legacy_dependencies_count: int
    dependencies: List[str] = Field(default_factory=list, description="Downstream relational system connections.")
    operational_history_notes: str

class LineageRegistry:
    """Manages file-based persistence for tracking infrastructure heritage baselines."""

    def __init__(self, storage_path: str = "src/medicine_wheel_ops/storage/registry.json"):
        self.storage_path = storage_path
        self._initialize_storage()

    def _initialize_storage(self):
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w") as f:
                json.dump({}, f)

    def register_profile(self, profile: SystemProfile) -> None:
        """Persists an infrastructure profile into the lineage database registry."""
        with open(self.storage_path, "r") as f:
            data = json.load(f)
        
        data[profile.system_id] = profile.model_dump()
        
        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_profile(self, system_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves historical heritage data for a specific infrastructure boundary."""
        with open(self.storage_path, "r") as f:
            data = json.load(f)
        return data.get(system_id)
