from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # 3 phases (0, 1, 2) to simulate the 3 parts described in the problem
        phase = 0
        if (nums[1] <= nums[0]):
            return False
        for index, num in enumerate(nums):
            if (index == 0):
                continue
            
            if (nums[index] == nums[index-1]):
                return False
            
            if (phase == 0 and nums[index] < nums[index-1]):
                phase += 1
            elif (phase == 1 and nums[index] > nums[index-1]):
                phase += 1
            elif (phase == 2 and nums[index] < nums[index-1]):
                return False
        return phase == 2
    
                