"""
Implements the Custom Alert Classification Trigger.
Categorizes system anomalies into ecological states based on resource reciprocity.
"""

from pydantic import BaseModel
from medicine_wheel_ops.telemetry.spike_detector import SpikeAssessmentResult
from medicine_wheel_ops.pipeline.webwork_assessor import WebworkScore, WebworkAssessor

class EcologicalAlert(BaseModel):
    """Schema representing a synthesized holistic system alert."""
    system_id: str
    classification: str # ADAPTIVE_SHIFT, SYSTEMIC_DISRUPTION, ECOSYSTEM_TRAUMA
    urgency: str        # LOW, MEDIUM, CRITICAL
    summary: str

class AlertClassifier:
    """Synthesizes time-series anomalies and multidimensional footprints into prioritized alerts."""

    def __init__(self, max_allowed_variance: float = 1.5):
        self.max_allowed_variance = max_allowed_variance
        self.assessor = WebworkAssessor()

    def classify_event(self, spike_result: SpikeAssessmentResult, footprint: WebworkScore) -> EcologicalAlert:
        """
        Evaluates a time-series spike against the system's overall balance.
        If a spike occurs but the webwork remains balanced, it is classified as a healthy adaptive shift.
        """
        variance = self.assessor.calculate_ecosystem_variance(footprint)
        is_balanced = variance <= self.max_allowed_variance and footprint.operational_burnout < 3.5

        # Logic Matrix Mapping
        if spike_result.verdict == "CRITICAL_SPIKE" and not is_balanced:
            return EcologicalAlert(
                system_id=spike_result.system_id,
                classification="SYSTEMIC_DISRUPTION",
                urgency="CRITICAL",
                summary=f"Critical extractive drain detected on {spike_result.system_id}. System variance is unstable ({variance})."
            )
        
        if spike_result.verdict == "CRITICAL_SPIKE" and is_balanced:
            return EcologicalAlert(
                system_id=spike_result.system_id,
                classification="ADAPTIVE_SHIFT",
                urgency="LOW",
                summary=f"System {spike_result.system_id} experienced a critical spike but successfully absorbed the stress via adaptive loops."
            )

        if spike_result.verdict == "DEVIANT" and not is_balanced:
            return EcologicalAlert(
                system_id=spike_result.system_id,
                classification="SYSTEMIC_DISRUPTION",
                urgency="MEDIUM",
                summary=f"Deviant behavior on {spike_result.system_id} combined with an unbalanced resource footprint."
            )

        return EcologicalAlert(
            system_id=spike_result.system_id,
            classification="ADAPTIVE_SHIFT",
            urgency="LOW",
            summary=f"System {spike_result.system_id} is operating within sustainable parameters."
        )
