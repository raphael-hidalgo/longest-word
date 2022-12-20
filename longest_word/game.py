# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random
from typing import List
from nltk.corpus import words

class Game:
    def __init__(self) -> List[str]:
        """Attribute a random grid to size 9"""
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if word == "":
            return False
        for letter in word:
            if letter not in self.grid:
                return False
        if word.lower() not in words.words():
            return False
        return True
