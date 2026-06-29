from dataclasses import dataclass, field
from typing import List

from .exercise import Exercise


@dataclass
class WeeklyTest:
    week_number: int

    mcqs: List[Exercise] = field(default_factory=list)
    fill_in_the_blanks: List[Exercise] = field(default_factory=list)
    unscramble: List[Exercise] = field(default_factory=list)
    dictation: List[Exercise] = field(default_factory=list)
    match_the_following: List[Exercise] = field(default_factory=list)