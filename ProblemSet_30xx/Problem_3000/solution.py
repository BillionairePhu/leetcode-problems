from typing import List
from math import sqrt

class Solution:
  def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    result, max_diag = [], 0
    for dimension in dimensions:
      diag = sqrt(dimension[0]**2 + dimension[1]**2)
      if (diag > max_diag):
        result = [dimension[0] * dimension[1]]
        max_diag = diag
      elif (diag == max_diag):
        result.append(dimension[0] * dimension[1])

    return max(result)
  
s = Solution()
print(s.areaOfMaxDiagonal([[2,6],[5,1],[3,10],[8,4]]))