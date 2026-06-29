from enum import Enum


class ExerciseType(Enum):
    MCQ = "Multiple Choice"

    FILL_IN_THE_BLANK = "Fill in the Blank"

    UNSCRAMBLE = "Unscramble"

    MATCH_THE_FOLLOWING = "Match the Following"

    DICTATION = "Dictation"

    SPELLING = "Spelling"

    TRUE_FALSE = "True / False"

    SHORT_ANSWER = "Short Answer"

    CHALLENGE = "Challenge"