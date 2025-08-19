from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        consecutiveZeros = 0
        result = 0
        for num in nums:
            if (num == 0):
                consecutiveZeros += 1
                result += consecutiveZeros
            else:
                consecutiveZeros = 0
        return result