from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxi = max(nums)
        myset = set([num for num in nums if num >= 0])
        
        return sum(myset) if len(myset) > 0 else maxi
    
s = Solution()
print(s.maxSum([1,2,3,4,5]))
print(s.maxSum([1,1,0,1,1]))