from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n, result = len(nums) // 3, 0
        
        for i in range(n):
            result += nums[n + 2*i]
        
        return result
        
s = Solution()
print('Result', s.maximumMedianSum([2,1,3,2,1,3]))
print('Result', s.maximumMedianSum([1000, 1, 1]))