from typing import List


class Solution:
  def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    n = len(grid)
    for i in range(n):
      diag_vals = []
      for j in range(i+1):
        diag_vals.append(grid[n-1 -i + j][j])
      diag_vals.sort(reverse=True)
      for j in range(i+1):
        grid[n-1 -i + j][j] = diag_vals[j]
        
    for i in range(n-1):
      diag_vals = []
      for j in range(i+1):
        diag_vals.append(grid[j][n-1 -i + j])
      diag_vals.sort()
      for j in range(i+1):
        grid[j][n-1 -i + j] = diag_vals[j]
    return grid
      
s = Solution()
s.sortMatrix([
  [1,7,3],
  [9,8,2],
  [4,5,6]])