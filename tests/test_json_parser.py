"""
Unit verification suite for testing incoming external JSON payload translation wrappers.
"""

import pytest
from medicine_wheel_ops.telemetry.json_parser import JSONStreamParser

def test_parse_nested_external_api_json():
    parser = JSONStreamParser()
    
    # Simulating a messy, real-world third-party infrastructure webhook payload
    raw_api_data = {
        "metadata": {
            "target_id": "easi-api-gateway",
            "environment": "PRD"
        },
        "telemetry": {
            "cpu_utilization": 240.5,
            "memory_used_mb": 512.0,
            "optimizations_delivered": 300.0,
            "locks_released": 120.5
        }
    }
    
    metrics = parser.parse_raw_payload(raw_api_data)
    
    assert metrics.compute_cycles == 240.5
    assert metrics.memory_footprint == 512.0
    assert metrics.downstream_optimizations == 300.0
    assert metrics.context_dimensions["system_id"] == "easi-api-gateway"

def test_parse_malformed_string_graceful_recovery():
    parser = JSONStreamParser()
    broken_payload = "{ 'invalid_json': true, "
    
    metrics = parser.parse_string_payload(broken_payload)
    assert metrics.compute_cycles == 0.0
    assert metrics.context_dimensions["parsing_error"] == "malformed_json_string"
