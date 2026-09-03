"""
Implements relational co-dependency engines and system balance algorithms.
"""

from medicine_wheel_ops.engines.base_engine import SystemMetrics, EngineProtocol

class CoDependencyEngine(EngineProtocol):
    """Calculates extraction indices to track balance and network load."""
    
    def __init__(self, min_threshold: float = 0.75):
        self.min_threshold = min_threshold

    def calculate_sustainability(self, metrics: SystemMetrics) -> float:
        """
        Calculates the Reciprocity Index.
        Formula models the relationship between system resource extraction and downstream utility.
        """
        given = metrics.downstream_optimizations + metrics.shared_resource_release
        taken = metrics.compute_cycles + metrics.memory_footprint
        
        if taken == 0:
            return 1.0
            
        reciprocity_score = float(given / taken)
        return round(reciprocity_score, 4)

    def evaluate_node_adaptability(self, score: float) -> str:
        """Determines if a node is behaving extractively or harmoniously with dependencies."""
        if score >= self.min_threshold:
            return "DYNAMIC_BALANCE"
        return "EXTRACTIVE_DRAIN"
