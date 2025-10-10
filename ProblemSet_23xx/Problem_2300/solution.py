from bisect import bisect_left
from typing import List


class Solution:
  def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    result = []
    for spell in spells:
      satisfied_potion = success / spell
      index = bisect_left(potions, satisfied_potion)
      result.append(len(potions) - index)
    return result
  
s = Solution()
# print(s.successfulPairs([5,1,3], [1,2,3,4,5], 7))
print(s.successfulPairs([3,1,2], [8,5,8], 16))