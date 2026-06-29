from dataclasses import dataclass, field
from typing import List
from .word import Word
from .exercise import Exercise

@dataclass
class Lesson:
    day_number: int
    title: str
    words: List[Word] = field(default_factory=list)
    exercises: List[Exercise] = field(default_factory=list)