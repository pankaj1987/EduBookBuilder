from dataclasses import dataclass

from app.enums import Difficulty, Category


@dataclass
class Word:
    word: str
    pronunciation: str
    meaning: str
    sentence: str

    synonym: str
    antonym: str

    memory_trick: str
    picture_suggestion: str

    difficulty: Difficulty

    category: Category

    root_word: str = ""
    prefix: str = ""
    suffix: str = ""
    phonics: str = ""