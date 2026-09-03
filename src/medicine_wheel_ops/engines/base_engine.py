"""
Abstract base definitions and data types representing contract agreements
for mathematical frameworks across system operations.
"""

from typing import Protocol, Dict, Any
from pydantic import BaseModel, Field

class SystemMetrics(BaseModel):
    """Immutable data structure holding multi-dimensional workload statistics."""
    compute_cycles: float = Field(..., description="CPU or processing intensity consumed.")
    memory_footprint: float = Field(..., description="Shared allocation footprint in MB.")
    downstream_optimizations: float = Field(..., description="Calculated architectural value passed down.")
    shared_resource_release: float = Field(..., description="Rate of resource locking relinquishment.")
    context_dimensions: Dict[str, Any] = Field(default_factory=dict, description="Metadata tags.")

class EngineProtocol(Protocol):
    """Protocol structure enforcing standard interface contracts for analytical modules."""
    def calculate_sustainability(self, metrics: SystemMetrics) -> float:
        """
        Computes the core health index of a component boundary context.
        Note: The '...' below is an explicit Python Protocol syntax designator.
        """
        ...
