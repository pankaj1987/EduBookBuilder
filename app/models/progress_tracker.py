from dataclasses import dataclass, field
from typing import List


@dataclass
class ProgressTracker:
    completed_lessons: List[int] = field(default_factory=list)

    weekly_scores: List[int] = field(default_factory=list)

    monthly_scores: List[int] = field(default_factory=list)

    final_score: int = 0