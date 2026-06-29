from dataclasses import dataclass, field
from typing import List

from .exercise import Exercise


@dataclass
class MockTest:
    title: str

    questions: List[Exercise] = field(default_factory=list)

    answer_key: List[str] = field(default_factory=list)