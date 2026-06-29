from dataclasses import dataclass


@dataclass
class Exercise:
    question: str
    answer: str
    marks: int
    exercise_type: str