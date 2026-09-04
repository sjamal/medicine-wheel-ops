"""
Unit verification suite verifying cyclical log window rotation and data preservation bounds.
"""

import os
from medicine_wheel_ops.storage.state_logger import CyclicalStateLogger

def test_cyclical_state_truncation():
    test_log = "tests/test_history.json"
    logger = CyclicalStateLogger(file_path=test_log, max_window=3)
    
    # Append values past max threshold window parameters
    logger.append_state("cluster-x", 10.0)
    logger.append_state("cluster-x", 20.0)
    logger.append_state("cluster-x", 30.0)
    window = logger.append_state("cluster-x", 40.0)
    
    # Assert sliding limit strictly capped at maximum window width dimension
    assert len(window) == 3
    # 10.0 is cleanly dropped from history loop, tracking elements 20, 30, and 40
    assert window == [20.0, 30.0, 40.0]
    
    if os.path.exists(test_log):
        os.remove(test_log)
