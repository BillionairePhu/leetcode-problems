# Write your solution here
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result = 0
        prevNum = nums[0]
        for i in range(1, len(nums) - 1):
            if (nums[i] == nums[i+1]):
                continue
            if (nums[i] > prevNum and nums[i] > nums[i+1]):
                result += 1
            elif (nums[i] < prevNum and nums[i] < nums[i+1]):
                result += 1
            prevNum = nums[i]
        return result