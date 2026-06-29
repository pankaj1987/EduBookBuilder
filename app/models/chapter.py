from dataclasses import dataclass, field
from typing import List

from .lesson import Lesson


@dataclass
class Chapter:
    number: int
    title: str
    summary: str

    lessons: List[Lesson] = field(default_factory=list)