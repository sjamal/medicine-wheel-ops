"""
Implements the Time-Series Assessment Engine for detecting metric spikes.
Evaluates variance trends over sliding windows to prevent static limit failures.
"""

from typing import List, Dict, Any
from pydantic import BaseModel, Field

class SpikeAssessmentResult(BaseModel):
    """Data schema representing the output evaluation of a telemetry anomaly review."""
    system_id: str
    metric_name: str
    current_value: float
    rolling_mean: float
    variance_ratio: float
    verdict: str = Field(..., description="Evaluation verdict: NOMINAL, DEVIANT, or CRITICAL_SPIKE.")

class TelemetrySpikeDetector:
    """Evaluates historical data queues to detect dynamic systemic stress anomalies."""

    def __init__(self, deviation_threshold: float = 2.0):
        self.deviation_threshold = deviation_threshold

    def evaluate_window(self, system_id: str, metric_name: str, current_value: float, window_history: List[float]) -> SpikeAssessmentResult:
        """
        Calculates moving statistics over a window array.
        Flags critical shifts using variance ratios instead of hard zero-tolerance rules.
        """
        if not window_history:
            return SpikeAssessmentResult(
                system_id=system_id, metric_name=metric_name, current_value=current_value,
                rolling_mean=current_value, variance_ratio=1.0, verdict="NOMINAL"
            )

        rolling_mean = sum(window_history) / len(window_history)
        
        # Guard against zero-division states on pristine baselines
        if rolling_mean == 0:
            variance_ratio = 1.0 if current_value == 0 else float('inf')
        else:
            variance_ratio = float(current_value / rolling_mean)

        # Dynamic Threshold Verdict Mapping
        if variance_ratio >= (self.deviation_threshold * 1.5):
            verdict = "CRITICAL_SPIKE"
        elif variance_ratio >= self.deviation_threshold:
            verdict = "DEVIANT"
        else:
            verdict = "NOMINAL"

        return SpikeAssessmentResult(
            system_id=system_id,
            metric_name=metric_name,
            current_value=round(current_value, 2),
            rolling_mean=round(rolling_mean, 2),
            variance_ratio=round(variance_ratio, 2),
            verdict=verdict
        )
