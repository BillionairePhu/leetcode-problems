class Solution:
    def smallestNumber(self, n: int) -> int:
        result = 1
        while result < n:
            result <<= 1
            result += 1
        return result