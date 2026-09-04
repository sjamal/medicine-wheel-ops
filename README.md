# Medicine Wheel Operations Engine (`medicine-wheel-ops`)

An analytical implementation project translating the place-based principles of Dr. Jennifer Grenz's *Medicine Wheel for the Planet* into software engineering architectures, microservice simulations, and programmatic CI/CD governance patterns.

## Framework Quadrants Covered
- **North (Elder Wisdom):** Long-Baseline System Heritage analytics via Git history tracking.
- **East (Deconstructing Separation):** Webwork multidimensional balanced metrics over zero-sum risk matrices.
- **South (Active Stewardship):** Technical Debt Reciprocity gatekeeper preventing exploitative feature harvesting.
- **West (Relational Decision-Making):** Quantifiable Algorithmic Governance design protocols.

## Verification & Execution Examples

### 1. Programmatic Calculation of Reciprocity Scores
To run a sustainability calculation on an active workload matrix directly in your python shell:
```python
from medicine_wheel_ops.engines.base_engine import SystemMetrics
from medicine_wheel_ops.engines.dependency_engine import CoDependencyEngine

# Establish metrics footprint
metrics = SystemMetrics(
    compute_cycles=120.0, 
    memory_footprint=64.0, 
    downstream_optimizations=150.0, 
    shared_resource_release=40.0
)

engine = CoDependencyEngine(min_threshold=0.75)
score = engine.calculate_sustainability(metrics)
print(f"Reciprocity Index: {score}")  # Returns float ratio
print(f"System Balance: {engine.evaluate_node_adaptability(score)}")
```

### 2. Simulating Multi-Agent Ecosystem Adaptability
To execute a self-healing loop simulation under sudden load anomalies:
```python
from medicine_wheel_ops.engines.evolution_engine import EcosystemSimulation

# Instantiate cluster nodes
sim = EcosystemSimulation(agent_ids=["auth-service", "data-pipeline"])

# Inject massive stress exceeding load limits to trigger adaptation bounds
status = sim.inject_systemic_stress("auth-service", 150.0)
print(f"Post-Stress Status: {status}") # Returns 'ADAPTED_RECOVERY' instead of crashing
```

### 3. Running Webwork Multidimensional Balance Checks
To execute a variance assessment verifying operational burnout thresholds:
```python
from medicine_wheel_ops.pipeline.webwork_assessor import WebworkAssessor, WebworkScore

assessor = WebworkAssessor()
score = WebworkScore(
    system_integrity=4.5,
    operational_burnout=2.1,  # Safe toil baseline
    resource_overhead=1.5,
    knowledge_equity=4.0
)

balanced = assessor.is_balanced(score, max_variance=1.0)
print(f"Deployment Alignment Verification: {balanced}") # Returns True
```

### 4. Pluggable Telemetry Stream Hydration
To switch between synthetic generation streams and production APIs:
```python
from medicine_wheel_ops.telemetry.hydrator import SyntheticHydrator, RealAPIHttpSource

# Option A: Run via Synthetic Noise Hydrator
stream_source = SyntheticHydrator()
print(stream_source.fetch_current_telemetry("cluster-a"))

# Option B: Drop-in live production HTTP API source seamlessly
production_source = RealAPIHttpSource(api_endpoint="https://api.internal", bearer_token="xyz")
print(production_source.fetch_current_telemetry("cluster-a"))
```
