import math


class Solution:
  def maxDistinctElements(self, nums: list[int], k: int) -> int:
    nums.sort()
    
    result = 0
    curr = -math.inf
    for num in nums:
      curr = max(curr, num - k)
      if (num - curr <= k and num - curr >= -k):
        result += 1
        curr += 1
    return result

s = Solution()
print("Result", s.maxDistinctElements([1,2,2,3,3,4], 2))
print("Result", s.maxDistinctElements([4,4,4], 1))