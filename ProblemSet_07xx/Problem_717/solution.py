from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        word = ""
        last_word = ""
        valid_words = ["10", "11", "0"]
        for bit in bits:
            word += str(bit)
            if (word in valid_words):
                last_word = word
                word = ""
        return last_word == "0"