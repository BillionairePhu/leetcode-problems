from typing import List

class Solution:
  def minimumTotal(self, grid: List[List[int]]) -> int:
    for i in range(1, len(grid)):
      for j in range(len(grid[i])):
        considers = []
        if (j > 0):
          considers.append(grid[i-1][j-1])
        if (j < len(grid[i]) - 1):
          considers.append(grid[i-1][j])
        grid[i][j] = grid[i][j] + min(considers)
    return min(grid[-1])