"""Verifies code tending validation constraints."""
import os
from medicine_wheel_ops.pipeline.debt_broker import DebtBroker

def test_empty_repo_graceful_pass():
    broker = DebtBroker(repo_path=".")
    stats = broker.parse_commit_stewardship()
    assert "tending_ratio" in stats
