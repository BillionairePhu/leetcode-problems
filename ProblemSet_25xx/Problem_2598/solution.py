from math import inf
from typing import Counter, List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = Counter()
        for num in nums:
            counter[num % value] += 1
            
        min_key, min_freq = inf, inf
        for i in range(value):
            if (counter[i] < min_freq):
                min_freq = counter[i]
                min_key = i
            
        print(min_key, min_freq)
        return min_freq * value + min_key

s = Solution()
print("Result", s.findSmallestInteger([1,-10,7,13,6,8], 5))
print("Result", s.findSmallestInteger([1,-10,7,13,6,8], 7))