from typing import Counter, List


class Solution:
  def repeatedNTimes(self, nums: List[int]) -> int:
    candidate1, vote1 = None, 0
    candidate2, vote2 = None, 0
    
    for num in nums:
      if (num == candidate1):
        vote1 += 1
      elif (num == candidate2):
        vote2 += 1
      elif (vote1 == 0):
        candidate1 = num
        vote1 += 1
      elif (vote2 == 0):
        candidate2 = num
        vote2 += 1
      else:
        vote1 -= 1
        vote2 -= 1
        
    if (nums.count(candidate1) > 1):
      return candidate1
    return candidate2
    
s = Solution()
print("Result", s.repeatedNTimes([1,2,3,3]))