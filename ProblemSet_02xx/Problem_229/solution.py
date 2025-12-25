from math import floor
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj1, count1 = None, 0
        maj2, count2 = None, 0
        
        for num in nums:
            if (num == maj1):
                count1 += 1
            elif (num == maj2):
                count2 += 1
            elif (count1 == 0):
                maj1 = num
                count1 = 1
            elif (count2 == 0):
                maj2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = []
        if (nums.count(maj1) > floor(len(nums)/3)):
            result.append(maj1)
        if (nums.count(maj2) > floor(len(nums)/3)):
            result.append(maj2)
        return result