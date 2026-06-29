from dataclasses import dataclass, field
from typing import List

from .chapter import Chapter
from .mock_test import MockTest


@dataclass
class Book:
    title: str
    subtitle: str
    author: str
    grade: str
    language: str

    chapters: List[Chapter] = field(default_factory=list)
    mock_tests: List[MockTest] = field(default_factory=list)

    certificate = None
    progress_tracker = None