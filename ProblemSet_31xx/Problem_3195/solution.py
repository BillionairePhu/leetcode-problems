from typing import List


class Solution:
  def minimumArea(self, grid: List[List[int]]) -> int:
    left, right, top, bot = None, None, None, None
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if (grid[i][j] == 1):
          left = min(j, left) if left != None else j
          right = max(j, right) if right != None else j
          top = min(i, top) if top != None else i
          bot = max(i, bot) if bot != None else i
    if left == None:
      return 0
    print(left, right, top, bot)
    return (right - left + 1) * (bot - top + 1)
  
s = Solution()
print("Result", s.minimumArea([[0,1,0],[1,0,1]]))