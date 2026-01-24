from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        
        for i in range(len(nums) // 2):
            result = max(result, nums[i] + nums[len(nums)-1-i])
        
        return result

s = Solution()
print("Result", s.minPairSum([3,5,4,2,4,6]))