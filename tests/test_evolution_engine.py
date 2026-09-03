"""
Unit verification suite for testing multi-agent adaptation and simulation resilience.
"""

from medicine_wheel_ops.engines.evolution_engine import EcosystemSimulation

def test_agent_adaptation_under_stress():
    """Ensures nodes execute self-healing adaptation instead of hard-crashing under heavy load."""
    sim = EcosystemSimulation(agent_ids=["auth-service"])
    
    # Verify starting conditions
    assert sim.agents["auth-service"].status == "HARMONIOUS"
    assert sim.agents["auth-service"].adaptation_count == 0

    # Inject stress exceeding load capacity to trigger an out-of-bounds self-healing loop
    result = sim.inject_systemic_stress("auth-service", 150.0)
    
    assert result == "ADAPTED_RECOVERY"
    assert sim.agents["auth-service"].adaptation_count == 1
    assert sim.agents["auth-service"].status == "HARMONIOUS"
    assert sim.agents["auth-service"].current_stress <= 100.0
