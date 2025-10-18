from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        small_index, large_index = 0, 0
        result = 0
        
        while large_index < len(nums):
            if (nums[large_index] > nums[small_index]):
                small_index += 1
                result += 1
            large_index += 1
        return result
    
s = Solution()
print(s.maximizeGreatness([1,3,5,2,1,3,1]))
print(s.maximizeGreatness([1,2,3,4]))