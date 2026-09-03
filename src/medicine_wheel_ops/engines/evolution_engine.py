"""
Implements multi-agent simulation layers and dynamic ecosystem adaptability rules.
Models code structures as responsive biological nodes capable of self-healing.
"""

import random
from typing import List, Dict, Any
from pydantic import BaseModel, Field

class SimulationAgent(BaseModel):
    """Represents an isolated processing entity or microservice thread within the ecosystem."""
    agent_id: str
    load_capacity: float = Field(100.0, description="Maximum operational processing threshold.")
    current_stress: float = Field(0.0, description="Calculated resource consumption stress.")
    adaptation_count: int = Field(0, description="Tracked self-healing events executed.")
    status: str = Field("HARMONIOUS", description="State designation: HARMONIOUS, STRESSED, or SHATTERED.")

class EcosystemSimulation:
    """Manages multi-agent feedback loops to evaluate dynamic systemic resilience under load."""

    def __init__(self, agent_ids: List[str]):
        self.agents: Dict[str, SimulationAgent] = {
            aid: SimulationAgent(agent_id=aid) for aid in agent_ids
        }

    def inject_systemic_stress(self, target_id: str, stress_magnitude: float) -> str:
        """
        Applies a traffic spike or resource load to a specific agent.
        Triggers an adaptation loop if stress thresholds are breached.
        """
        if target_id not in self.agents:
            return "UNKNOWN_NODE"

        agent = self.agents[target_id]
        agent.current_stress += stress_magnitude

        # Evaluate Adaptation Loop Condition (Ecosystem Self-Healing)
        if agent.current_stress > agent.load_capacity:
            return self._execute_adaptation_loop(agent)
        
        if agent.current_stress > (agent.load_capacity * 0.7):
            agent.status = "STRESSED"
        else:
            agent.status = "HARMONIOUS"
        return agent.status

    def _execute_adaptation_loop(self, agent: SimulationAgent) -> str:
        """
        Instead of throwing a hard failure or crashing (The 'Eden Ecology' flaw),
        the agent dynamically sheds non-critical logic and self-heals.
        """
        agent.adaptation_count += 1
        # Mitigate stress through adaptive dampening (e.g., asynchronous load-shedding)
        dampening_factor = random.uniform(0.4, 0.6)
        agent.current_stress = agent.load_capacity * dampening_factor
        agent.status = "HARMONIOUS"
        return "ADAPTED_RECOVERY"
