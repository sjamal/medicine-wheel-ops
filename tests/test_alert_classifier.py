"""
Unit verification suite for the Custom Alert Classification Trigger.
"""

import pytest
from medicine_wheel_ops.pipeline.alert_classifier import AlertClassifier
from medicine_wheel_ops.telemetry.spike_detector import SpikeAssessmentResult
from medicine_wheel_ops.pipeline.webwork_assessor import WebworkScore

def test_classify_healthy_adaptive_shift():
    classifier = AlertClassifier()
    
    spike = SpikeAssessmentResult(
        system_id="easi-web-pod", metric_name="cpu",
        current_value=95.0, rolling_mean=20.0, variance_ratio=4.75, verdict="CRITICAL_SPIKE"
    )
    # Footprint remains balanced despite the spike
    footprint = WebworkScore(system_integrity=4.0, operational_burnout=2.0, resource_overhead=1.0, knowledge_equity=4.5)
    
    alert = classifier.classify_event(spike, footprint)
    assert alert.classification == "ADAPTIVE_SHIFT"
    assert alert.urgency == "LOW"

def test_classify_extractive_disruption():
    classifier = AlertClassifier()
    
    spike = SpikeAssessmentResult(
        system_id="easi-web-pod", metric_name="cpu",
        current_value=95.0, rolling_mean=20.0, variance_ratio=4.75, verdict="CRITICAL_SPIKE"
    )
    # Footprint is highly unbalanced (severe operational burnout)
    footprint = WebworkScore(system_integrity=4.5, operational_burnout=4.8, resource_overhead=4.0, knowledge_equity=1.5)
    
    alert = classifier.classify_event(spike, footprint)
    assert alert.classification == "SYSTEMIC_DISRUPTION"
    assert alert.urgency == "CRITICAL"
