# Write your solution here
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0
        for fruit in fruits:
            isPlaced = False
            for j in range(len(baskets)):
                if (baskets[j] >= fruit):
                    baskets[j] = 0
                    isPlaced = True
                    break
            if (not isPlaced):
                result += 1
        return result
                