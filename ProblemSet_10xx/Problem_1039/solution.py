from typing import List


class Solution:
  def minScoreTriangulation(self, values: List[int]) -> int:
    if len(values) == 3:
      return values[0] * values[1] * values[2]
    
    mins = []
    for i in range(len(values)):
      new_values = values.copy()
      new_values.pop(i)
      popped_triangle = values[i] * values[i-1] * values[(i+1) % len(values)]
      mins.append(popped_triangle + self.minScoreTriangulation(new_values))
    
    return min(mins)
  
s = Solution()
print(s.minScoreTriangulation([1,3,1,4,1,5]))