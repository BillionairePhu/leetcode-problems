# Write your solution here
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_value = 0
        for num in nums:
            max_value |= num
            
        def recur(temp_value: int, index: int):
            if (temp_value == max_value):
                return 2 ** (len(nums) - index)
            
            if (index >= len(nums)):
                return 0
            
            return recur(temp_value, index+1) + recur(temp_value|nums[index], index+1)
        
        return recur(0, 0)
    
    
    
s = Solution()
print('Result', s.countMaxOrSubsets([3,1]))
print('Result', s.countMaxOrSubsets([2,2,2]))
print('Result', s.countMaxOrSubsets([3,2,1,5]))