# Architectural Decision Record 0003: Pipeline Reciprocity Enforcement

## Status
Accepted

## Context
Code bases are often treated as open extraction pits where features are continuously harvested without maintaining technical debt.

## Decision
Continuous Integration loops will track file modifications to compute a Tending Ratio. Builds will be blocked if functionality is introduced without an equivalent, reciprocal unit of code refactoring or pruning.
