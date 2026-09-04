"""
Unit verification suite verifying the pluggable Data Ingestion engine contracts.
"""

from medicine_wheel_ops.telemetry.hydrator import SyntheticHydrator, RealAPIHttpSource
from medicine_wheel_ops.engines.base_engine import SystemMetrics

def test_synthetic_hydrator_emits_valid_metrics():
    hydrator = SyntheticHydrator()
    metrics = hydrator.fetch_current_telemetry("ngsis-core-cluster")
    
    assert isinstance(metrics, SystemMetrics)
    assert metrics.compute_cycles > 0.0
    assert metrics.context_dimensions["system_id"] == "ngsis-core-cluster"
    assert metrics.context_dimensions["source"] == "synthetic_hydrator"

def test_api_source_adheres_to_protocol():
    api_source = RealAPIHttpSource(api_endpoint="https://monitoring.internal", bearer_token="token")
    metrics = api_source.fetch_current_telemetry("easi-app-server")
    
    assert metrics.context_dimensions["source"] == "live_http_api"
    assert metrics.downstream_optimizations == 160.0
