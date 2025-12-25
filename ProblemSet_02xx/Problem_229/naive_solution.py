from typing import Counter, List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        for key, value in Counter(nums).items():
            if (value > (len(nums) // 3)):
                result.append(key)
        return result