"""
Unit verification suite checking system lineage tracking and relational dependency data layers.
"""

import os
from medicine_wheel_ops.storage.lineage_registry import LineageRegistry, SystemProfile

def test_profile_registration_lifecycle():
    test_db = "tests/test_registry.json"
    registry = LineageRegistry(storage_path=test_db)
    
    profile = SystemProfile(
        system_id="api-gateway-node",
        historical_baseline_years=5,
        criticality_tier=1,
        legacy_dependencies_count=2,
        dependencies=["auth-service-pod", "backend-db-cluster"],
        operational_history_notes="Edge routing layer with mapped downstream cluster nodes."
    )
    
    registry.register_profile(profile)
    retrieved = registry.get_profile("api-gateway-node")
    
    assert retrieved is not None
    assert retrieved["dependencies"] == ["auth-service-pod", "backend-db-cluster"]
    assert retrieved["legacy_dependencies_count"] == 2
    
    if os.path.exists(test_db):
        os.remove(test_db)
