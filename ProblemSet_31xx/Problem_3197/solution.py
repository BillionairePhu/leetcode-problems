
from typing import List


class Solution:
  def minimumSum(self, grid: List[List[int]]) -> int:
    return self.split(grid, 0, len(grid[0])-1, 0, len(grid)-1, 3)
  
  def split(self, grid: list[list[int]], left: int, right: int, top: int, bot: int, shapes: int) -> int:
    if (shapes == 1):
      return self.getSize(grid, left, right, top, bot)
    
    result = len(grid) * len(grid[0])
    
    # Vertical split
    for i in range(top, bot):
      # Keep the bottom part, split the top part
      topSz = self.split(grid, left, right, top, i, shapes-1)
      botSz = self.split(grid, left, right, i+1, bot, 1)
      result = min(result, topSz + botSz)
      
      # Keep the top part, split the bottom part
      topSz = self.split(grid, left, right, top, i, 1)
      botSz = self.split(grid, left, right, i+1, bot, shapes-1)
      result = min(result, topSz + botSz)
    
    # Horizontal split
    for j in range(left, right):
      # Keep the left part, split the right part
      leftSz = self.split(grid, left, j, top, bot, 1)
      rightSz = self.split(grid, j+1, right, top, bot, shapes-1)
      result = min(result, leftSz + rightSz)
      
      # Keep the right part, split the left part
      leftSz = self.split(grid, left, j, top, bot, shapes-1)
      rightSz = self.split(grid, j+1, right, top, bot, 1)
      result = min(result, leftSz + rightSz)
    
    return result
      
  
  def getSize(
      self, grid: list[list[int]],
      left: int, right: int, top: int, bot: int
    ) -> int:
    leftBound, rightBound, topBound, botBound = None, None, None, None
    for i in range(top, bot + 1):
      for j in range(left, right + 1):
        if (grid[i][j] == 1):
          leftBound = min(leftBound, j) if leftBound != None else j
          rightBound = max(rightBound, j) if rightBound != None else j
          topBound = min(topBound, i) if topBound != None else i
          botBound = max(botBound, i) if botBound != None else i
    if (leftBound == None):
      return 0
    return (rightBound - leftBound + 1) * (botBound - topBound + 1)
  
s = Solution()
print(s.minimumSum([[1,0,1],[1,1,1]]))
# print(s.minimumSum([[1,0,1,0],[0,1,0,1]]))
# print(s.minimumSum([
#   [0,0,0,1,0],
#   [0,0,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,0,0],
#   [0,0,1,0,0]]))