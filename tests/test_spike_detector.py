"""
Unit verification suite for checking the time-series metric anomaly spike calculator.
"""

import pytest
from medicine_wheel_ops.telemetry.spike_detector import TelemetrySpikeDetector

def test_nominal_window_evaluation():
    detector = TelemetrySpikeDetector(deviation_threshold=2.0)
    history = [10.0, 12.0, 11.0, 9.0, 10.5]
    
    result = detector.evaluate_window("test-app", "cpu_stress", 11.5, history)
    assert result.verdict == "NOMINAL"
    assert result.variance_ratio < 2.0

def test_critical_spike_evaluation():
    detector = TelemetrySpikeDetector(deviation_threshold=2.0)
    history = [10.0, 10.0, 10.0, 10.0]
    
    # Value is 4x higher than rolling baseline, triggering critical flag bounds
    result = detector.evaluate_window("test-app", "cpu_stress", 40.0, history)
    assert result.verdict == "CRITICAL_SPIKE"
    assert result.variance_ratio == 4.0
