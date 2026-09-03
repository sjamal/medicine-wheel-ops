"""
Unit verification suite checking system lineage tracking and data persistence layers.
"""

import os
from medicine_wheel_ops.storage.lineage_registry import LineageRegistry, SystemProfile

def test_profile_registration_lifecycle():
    test_db = "tests/test_registry.json"
    registry = LineageRegistry(storage_path=test_db)
    
    profile = SystemProfile(
        system_id="ngsis-test-cluster",
        historical_baseline_years=5,
        criticality_tier=0,
        legacy_dependencies_count=14,
        operational_history_notes="Core database layer with deep legacy dependency matrices."
    )
    
    registry.register_profile(profile)
    retrieved = registry.get_profile("ngsis-test-cluster")
    
    assert retrieved is not None
    assert retrieved["criticality_tier"] == 0
    assert retrieved["legacy_dependencies_count"] == 14
    
    # Cleanup volatile tracking artifacts
    if os.path.exists(test_db):
        os.remove(test_db)
