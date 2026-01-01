from math import inf
from typing import List
from sortedcontainers import SortedList


class Solution:
  def maximumScore(self, nums: List[int]) -> int:
    prefixSum = 0
    sortedList = SortedList(nums)
    max_score = -inf
    
    for num in nums[0:len(nums)-1]:
      sortedList.remove(num)
      prefixSum += num
      suffixMin = sortedList[0]
      max_score = max(max_score, prefixSum - suffixMin)
      
    return max_score
  
s = Solution()
print(s.maximumScore([10,-1,3,-4,-5]))