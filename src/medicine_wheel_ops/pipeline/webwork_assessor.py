"""
Implements the circular Webwork Assessment model across system boundaries.
"""

from pydantic import BaseModel, Field

class WebworkScore(BaseModel):
    """Data representation of a four-dimensional circular impact score mapping the quadrants."""
    system_integrity: float = Field(..., ge=0.0, le=5.0)
    operational_burnout: float = Field(..., ge=0.0, le=5.0)
    resource_overhead: float = Field(..., ge=0.0, le=5.0)
    knowledge_equity: float = Field(..., ge=0.0, le=5.0)

class WebworkAssessor:
    """Evaluates multi-dimensional balance constraints across deployment landscapes."""

    @staticmethod
    def calculate_ecosystem_variance(score: WebworkScore) -> float:
        """
        Measures the variance between the four quadrants.
        High variance signifies an uneven systemic impact (e.g., speed bought with burnout).
        """
        dimensions = [
            score.system_integrity,
            5.0 - score.operational_burnout,  # Invert burnout so higher values are balanced
            5.0 - score.resource_overhead,   # Invert resource footprint overhead costs
            score.knowledge_equity
        ]
        
        mean = sum(dimensions) / 4.0
        variance = sum((x - mean) ** 2 for x in dimensions) / 4.0
        return round(float(variance), 4)

    def is_balanced(self, score: WebworkScore, max_variance: float = 1.0) -> bool:
        """Evaluates whether an infrastructure proposal complies with holistic safety tolerances."""
        variance = self.calculate_ecosystem_variance(score)
        return variance <= max_variance and score.operational_burnout < 3.5
