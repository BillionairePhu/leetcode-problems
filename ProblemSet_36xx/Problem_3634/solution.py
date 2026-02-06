from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        begin = 0
        end = 0
        result = len(nums)
        while begin < len(nums):
            while end < len(nums) and nums[begin] * k >= nums[end]:
                end += 1
            result = min(result, len(nums) - (end - begin))
            begin += 1
        return result
    
s = Solution()
# print("Result", s.minRemoval([8],1))
print("Result", s.minRemoval([2,1,5],2))
print("Result", s.minRemoval([4,1.5,7,8],2))
print("Result", s.minRemoval([1,6,2,9], 3))