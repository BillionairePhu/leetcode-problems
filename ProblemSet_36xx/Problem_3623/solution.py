from math import comb
from typing import Counter, List


class Solution:
  def countTrapezoids(self, points: List[List[int]]) -> int:
    rows = Counter()
    result = 0
    
    for x, y in points:
      rows[y] += 1
    
    row_items =  []
    for row in rows.values():
      if (row >= 2):
        row_items.append(comb(row,2))
        
    row_sum = sum(row_items)
    
    for i in range(len(row_items)):
      result += row_items[i] * (row_sum - row_items[i])
    
    return (result // 2) % (10**9 + 7)
    
s = Solution()
print("Result", s.countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]]))
print("Result", s.countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]]))