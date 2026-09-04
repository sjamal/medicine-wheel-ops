# Architectural Decision Record 0002: Modular Ecosystem Metrics

## Status
Accepted

## Context
Standard system monitoring uses flat, isolated consumption limits (e.g., CPU > 90%). This reflects an extractive approach that ignores interdependence.

## Decision
We choose to evaluate microservices by their Reciprocity Index ($R$). A node is flagged as unstable if its resource extraction overhead outpaces the downstream processing optimizations it passes to neighboring components.
