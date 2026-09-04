"""
Production Command Line Interface Wrapper for the Medicine Wheel Operations Engine.
"""

import sys
import argparse
from medicine_wheel_ops.telemetry.hydrator import SyntheticHydrator
from medicine_wheel_ops.telemetry.spike_detector import TelemetrySpikeDetector
from medicine_wheel_ops.pipeline.webwork_assessor import WebworkScore
from medicine_wheel_ops.pipeline.alert_classifier import AlertClassifier

def handle_scan(args):
    """Executes a diagnostic scan, evaluates spikes, and runs alert classification."""
    print(f"=== Initiating Ingestion Scan on System Target: {args.system} ===")
    
    # Dynamically inject an intentional spike if forced via argument flag
    if args.force_spike:
        hydrator = SyntheticHydrator(baseline_compute=450.0, baseline_memory=128.0)
    else:
        hydrator = SyntheticHydrator()
        
    metrics = hydrator.fetch_current_telemetry(args.system)
    
    detector = TelemetrySpikeDetector(deviation_threshold=1.8)
    mock_history = [100.0, 110.0, 95.0, 105.0, 102.0]
    
    spike_result = detector.evaluate_window(
        system_id=args.system, metric_name="compute_cycles",
        current_value=metrics.compute_cycles, window_history=mock_history
    )
    
    # Generate an environmental footprint score to pass to the classifier
    footprint = WebworkScore(
        system_integrity=4.2,
        operational_burnout=args.burnout, # Controlled via input flag
        resource_overhead=1.5,
        knowledge_equity=4.0
    )
    
    classifier = AlertClassifier()
    alert = classifier.classify_event(spike_result, footprint)
    
    print(f"\n[Telemetry] CPU Cycles: {metrics.compute_cycles} | RAM: {metrics.memory_footprint}MB")
    print(f"[Analysis]  Spike Verdict: {spike_result.verdict} (Variance Ratio: {spike_result.variance_ratio})")
    print(f"----------------------------------------------------------------------")
    print(f"[ALARM TRIGGER] Classification: {alert.classification}")
    print(f"[ALARM TRIGGER] Urgency Level:  {alert.urgency}")
    print(f"[ALARM TRIGGER] Action Summary: {alert.summary}")

def main():
    parser = argparse.ArgumentParser(description="Medicine Wheel Operations Engine CLI Core Utility.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Ingestion Ingestion Scan Configuration Arguments
    scan_parser = subparsers.add_parser("scan", help="Run Ingestion scans and classify alerts.")
    scan_parser.add_argument("--system", type=str, required=True, help="Target application system cluster ID.")
    scan_parser.add_argument("--burnout", type=float, default=2.0, help="Simulated current team operational burnout (0-5).")
    scan_parser.add_argument("--force-spike", action="store_true", help="Force a high-load time-series anomaly.")

    args = parser.parse_args()
    
    if args.command == "scan":
        handle_scan(args)

if __name__ == "__main__":
    main()
