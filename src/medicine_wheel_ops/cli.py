"""
Production Command Line Interface Wrapper for the Medicine Wheel Operations Engine.
"""

import sys
import os
import argparse
from medicine_wheel_ops.telemetry.hydrator import SyntheticHydrator
from medicine_wheel_ops.telemetry.json_parser import JSONStreamParser
from medicine_wheel_ops.telemetry.spike_detector import TelemetrySpikeDetector
from medicine_wheel_ops.pipeline.webwork_assessor import WebworkScore
from medicine_wheel_ops.pipeline.alert_classifier import AlertClassifier
from medicine_wheel_ops.storage.state_logger import CyclicalStateLogger

def handle_scan(args):
    """Executes an ingestion scan, updates ancestral state history, and runs alert classification."""
    print(f"=== Initiating Ingestion Scan on System Target: {args.system} ===")
    
    # Decoupling Ingestion: Route to File Stream Parser if target file path provided
    if args.from_json and os.path.exists(args.from_json):
        print(f"[Ingestion] Parsing real external JSON log package stream: {args.from_json}")
        parser = JSONStreamParser()
        with open(args.from_json, "r") as f:
            metrics = parser.parse_string_payload(f.read())
    else:
        # Fall back to synthetic data streams
        if args.force_spike:
            hydrator = SyntheticHydrator(baseline_compute=450.0, baseline_memory=128.0)
        else:
            hydrator = SyntheticHydrator()
        metrics = hydrator.fetch_current_telemetry(args.system)
    
    # Ancestral Memory Mapping: Retrieve past execution context paths from local storage disk
    logger = CyclicalStateLogger()
    window_history = logger.append_state(args.system, metrics.compute_cycles)
    
    detector = TelemetrySpikeDetector(deviation_threshold=1.8)
    
    # Safe slice passes history omitting the active iteration entry to avoid target echo bias
    historical_slice = window_history[:-1] if len(window_history) > 1 else []
    
    spike_result = detector.evaluate_window(
        system_id=args.system, metric_name="compute_cycles",
        current_value=metrics.compute_cycles, window_history=historical_slice
    )
    
    footprint = WebworkScore(
        system_integrity=4.2,
        operational_burnout=args.burnout,
        resource_overhead=1.5,
        knowledge_equity=4.0
    )
    
    classifier = AlertClassifier()
    alert = classifier.classify_event(spike_result, footprint)
    
    print(f"\n[Telemetry] CPU Cycles: {metrics.compute_cycles} | RAM: {metrics.memory_footprint}MB")
    print(f"[Ancestral History] Sliding Window Active Count: {len(window_history)} frames")
    print(f"[Analysis]  Spike Verdict: {spike_result.verdict} (Variance Ratio: {spike_result.variance_ratio})")
    print(f"----------------------------------------------------------------------")
    print(f"[ALARM TRIGGER] Classification: {alert.classification}")
    print(f"[ALARM TRIGGER] Urgency Level:  {alert.urgency}")
    print(f"[ALARM TRIGGER] Action Summary: {alert.summary}")

def main():
    parser = argparse.ArgumentParser(description="Medicine Wheel Operations Engine CLI Core Utility.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Run ingestion scans and classify alerts.")
    scan_parser.add_argument("--system", type=str, required=True, help="Target application system cluster ID.")
    scan_parser.add_argument("--burnout", type=float, default=2.0, help="Simulated current team operational burnout (0-5).")
    scan_parser.add_argument("--force-spike", action="store_true", help="Force a high-load time-series anomaly.")
    scan_parser.add_argument("--from-json", type=str, help="Optional external file path stream source destination.")

    args = parser.parse_args()
    
    if args.command == "scan":
        handle_scan(args)

if __name__ == "__main__":
    main()
