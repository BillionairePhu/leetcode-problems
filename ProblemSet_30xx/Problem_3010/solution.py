from math import inf
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1, min2 = inf, inf
        for i in range(1, len(nums)):
            num = nums[i]
            if (num < min1):
                min2 = min1
                min1 = num
            elif (num < min2):
                min2 = num
        return nums[0] + min1 + min2
    
s = Solution()
print("Result", s.minimumCost([1,2,3,12]))