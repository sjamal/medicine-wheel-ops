"""
Implements pluggable JSON parsing adaptors to map messy external monitoring structures
or real enterprise REST API payloads into standardized SystemMetrics records.
"""

import json
from typing import Dict, Any
from medicine_wheel_ops.engines.base_engine import SystemMetrics

class JSONStreamParser:
    """Translates arbitrary external dictionary layouts into structured framework schemas."""

    @staticmethod
    def parse_raw_payload(payload: Dict[str, Any]) -> SystemMetrics:
        """
        Extracts metrics from standard nested cloud infrastructure shapes.
        Maps real-world fields safely with default rollbacks to prevent parsing drops.
        """
        # Accommodate standard API footprints (e.g., Datadog/Prometheus JSON payload shapes)
        telemetry = payload.get("telemetry", payload)
        system_metadata = payload.get("metadata", {})
        
        compute = telemetry.get("cpu_utilization", telemetry.get("compute_cycles", 0.0))
        memory = telemetry.get("memory_used_mb", telemetry.get("memory_footprint", 0.0))
        
        # Pull reciprocal optimizations or default values based on system health
        optimizations = telemetry.get("optimizations_delivered", telemetry.get("downstream_optimizations", 0.0))
        release_rate = telemetry.get("locks_released", telemetry.get("shared_resource_release", 0.0))

        return SystemMetrics(
            compute_cycles=float(compute),
            memory_footprint=float(memory),
            downstream_optimizations=float(optimizations),
            shared_resource_release=float(release_rate),
            context_dimensions={
                "system_id": system_metadata.get("target_id", "unknown_boundary"),
                "ingestion_format": "json_stream"
            }
        )

    def parse_string_payload(self, json_string: str) -> SystemMetrics:
        """Parses incoming serialized string payloads directly from REST endpoints or file drops."""
        try:
            data = json.loads(json_string)
            return self.parse_raw_payload(data)
        except json.JSONDecodeError:
            # Safe recovery fallback mirroring ecological preservation
            return SystemMetrics(
                compute_cycles=0.0, memory_footprint=0.0,
                downstream_optimizations=0.0, shared_resource_release=0.0,
                context_dimensions={"parsing_error": "malformed_json_string"}
            )
