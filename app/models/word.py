from dataclasses import dataclass


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

    difficulty: str

    category: str

    root_word: str = ""

    prefix: str = ""

    suffix: str = ""

    phonics: str = ""