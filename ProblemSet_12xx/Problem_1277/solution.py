from typing import List


class Solution:
  def countSquares(self, matrix: List[List[int]]) -> int:
    counts, result = matrix.copy(), 0
    
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if (matrix[i][j] == 1):
          leftSqrSz = counts[i-1][j] if i > 0 else 0
          topSqrSz = counts[i][j-1] if j > 0 else 0
          topLeftSqrSz = counts[i-1][j-1] if i > 0 and j > 0 else 0
          
          counts[i][j] = min(leftSqrSz, topSqrSz, topLeftSqrSz) + 1
          result += counts[i][j]
        else:
          counts[i][j] = 0
    return result