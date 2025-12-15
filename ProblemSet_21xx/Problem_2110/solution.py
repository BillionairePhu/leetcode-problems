from typing import List


class Solution:
  def getDescentPeriods(self, prices: List[int]) -> int:
    streak, result = 1, 1
    prev = prices[0]
    
    for price in prices[1:]:
      streak = streak + 1 if (price + 1 == prev) else 1
      result = result + streak
      prev = price
    return result

s = Solution()
print("Result", s.getDescentPeriods([3,2,1,4]))