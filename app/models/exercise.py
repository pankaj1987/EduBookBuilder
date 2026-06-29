from dataclasses import dataclass
from app.enums import ExerciseType

@dataclass
class Exercise:
    question: str
    answer: str
    marks: int
    exercise_type: ExerciseType