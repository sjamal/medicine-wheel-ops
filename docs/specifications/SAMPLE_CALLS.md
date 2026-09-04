# Verification Reference & Testing Guidelines

### Running the Operational Validation Suite
To execute all codified compliance modules, run the testing engine out of your terminal:
```bash
pytest -v
```

### Testing Specific Modules Independently
If you want to run validations targeting only the pluggable stream layers or the evolution loops:
```bash
# Execute telemetry hydrator verification only
pytest tests/test_hydrator.py -v

# Execute multi-agent resilience simulation tests only
pytest tests/test_evolution_engine.py -v
```

### Script Execution Verification via Module Path
To verify your project layout builds paths dynamically, execute the internal entry structures via python's module runtime environment:
```bash
python3 -m medicine_wheel_ops.cli
```
