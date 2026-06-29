from dataclasses import dataclass


@dataclass
class Certificate:
    student_name: str
    grade: str
    completion_date: str
    instructor: str