from typing import List


class Solution:
  def findDiagonalOrder(
      self, mat: List[List[int]]
    ) -> List[int]:
    result, m, n = [], len(mat)-1, len(mat[0])-1
    i, j, dir = 0, 0, 1
    count = 0
    while True:
      count += 1
      result.append(mat[i][j])
      if (i == m and j == n):
        break
      
      if (dir == 1):
        # If hit wall, go the other directions
        if (i == 0 or j == n):
          dir = -1
        # Moving
        if (i == 0 and j == n):
          i += 1
        elif (i == 0):
          j += 1
        elif (j == n):
          i += 1
        else:
          i -= 1
          j += 1
      else:
        # If hit wall, go the other directions
        if (i == m or j == 0):
          dir = 1
        # Moving
        if (i == m and j == 0):
          j += 1
        elif(i == m):
          j += 1
        elif (j == 0):
          i += 1
        else:
          i += 1
          j -= 1

    return result
  
s = Solution()
# print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder([[1]]))
    