"""
Pipeline component governing code stewardship metrics and maintenance balance thresholds.
"""

import os
from typing import Dict, Any
from git import Repo

class DebtBroker:
    """Enforces continuous maintenance policies based on active feature tracking."""
    
    def __init__(self, repo_path: str, required_ratio: float = 1.20):
        self.repo_path = repo_path
        self.required_ratio = required_ratio

    def parse_commit_stewardship(self, target_branch: str = "main") -> Dict[str, Any]:
        """
        Examines local Git history metrics to evaluate refactoring ratios.
        Tracks if deletions (tending) match or exceed additions (harvesting).
        """
        if not os.path.exists(os.path.join(self.repo_path, ".git")):
            return {"additions": 0, "deletions": 0, "tending_ratio": 0.0}
            
        repo = Repo(self.repo_path)
        try:
            commits = list(repo.iter_commits(target_branch, max_count=50))
        except Exception:
            return {"additions": 0, "deletions": 0, "tending_ratio": 1.0}
        
        total_additions = 0
        total_deletions = 0
        
        for commit in commits:
            stats = commit.stats.total
            total_additions += stats.get("additions", 0)
            total_deletions += stats.get("deletions", 0)
            
        ratio = float(total_deletions / total_additions) if total_additions > 0 else 1.0
        
        return {
            "additions": total_additions,
            "deletions": total_deletions,
            "tending_ratio": round(ratio, 4)
        }

    def verify_compliance(self, stats: Dict[str, Any]) -> bool:
        """Enforces a pipeline gate preventing feature extraction without refactoring stability."""
        return bool(stats["tending_ratio"] >= self.required_ratio)
