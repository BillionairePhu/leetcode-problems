# Write your solution here
from typing import List


class Solution:
  def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
    result = 0
    
    def areZeroAndTwo(a: int, b: int) -> bool:
      """Check if one number is 0 and the other is 2"""
      return (a - 1) * (b - 1) == -1
    
    prefix = [
      [
        # 1st: top left -> bottom right
        # 2nd: top right -> bottom left
        # 3rd: bottom left -> top right
        # 4th: bottom right -> top left
        [0,0,0,0] for _ in grid[0]
      ] for _ in grid
    ]
    
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        # Calculate 1st length
        if (i > 0 and j > 0):
          if areZeroAndTwo(grid[i][j], grid[i-1][j-1]):
            prefix[i][j][0] = prefix[i-1][j-1][0] + 1
        # Calculate 2nd length
        if (i > 0 and j < len(grid[0]) - 1):
          if areZeroAndTwo(grid[i][j], grid[i-1][j+1]):
            prefix[i][j][1] = prefix[i-1][j+1][1] + 1
            
    for i in range(len(grid))[::-1]:
      for j in range(len(grid[0])):
        # Calculate 3rd length
        if (i < len(grid) - 1 and j > 0):
          if areZeroAndTwo(grid[i][j], grid[i+1][j-1]):
            prefix[i][j][2] = prefix[i+1][j-1][2] + 1
        # Calculate 4th length
        if (i < len(grid) - 1 and j < len(grid[0]) - 1):
          if areZeroAndTwo(grid[i][j], grid[i+1][j+1]):
            prefix[i][j][3] = prefix[i+1][j+1][3] + 1
    
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if (grid[i][j] != 1):
          continue
        
        # Go top left
        index, stack = 1, 0
        while (i - index >= 0 and j - index >= 0):
          if not (areZeroAndTwo(stack, grid[i-index][j-index])):
            break
          stack = grid[i-index][j-index]
          # Consider 2nd length
          result = max(result, prefix[i-index][j-index][1] + index + 1)
          index += 1
          
        # Go top right
        index, stack = 1, 0
        while (i - index >= 0 and j + index <= len(grid[0]) - 1):
          if not (areZeroAndTwo(stack, grid[i-index][j+index])):
            break
          stack = grid[i-index][j+index]
          # Consider 4th length
          result = max(result, prefix[i-index][j+index][3] + index + 1)
          index += 1
          
        # Go bottom left
        index, stack = 1, 0
        while (i + index <= len(grid)-1 and j - index >= 0):
          if not (areZeroAndTwo(stack, grid[i+index][j-index])):
            break
          stack = grid[i+index][j-index]
          # Consider 1st length
          result = max(result, prefix[i+index][j-index][0] + index + 1)
          index += 1
          
        # Go bottom right
        index, stack = 1, 0
        while (i + index <= len(grid)-1 and j + index <= len(grid[0])-1):
          if not (areZeroAndTwo(stack, grid[i+index][j+index])):
            break
          stack = grid[i+index][j+index]
          # Consider 3rd length
          result = max(result, prefix[i+index][j+index][2] + index + 1)
          index += 1
        # print(i, j, result)
        result = max(result, 1)
    return result
  
s = Solution()
# print(s.lenOfVDiagonal(
#   [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
# ))
# print(s.lenOfVDiagonal(
#   [
#     [2,2,1,2,2],
#     [2,0,2,2,0],
#     [2,0,1,1,0],
#     [1,0,2,2,2],
#     [2,0,0,2,2]
#   ]
# ))
# print(s.lenOfVDiagonal(
#   [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
# ))
print(s.lenOfVDiagonal(
  [
    [1,1,1,2,0,0],
    [0,0,0,0,1,2]
  ]
))