from typing import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for key, value in counter.items():
            if (value > 1):
                return key