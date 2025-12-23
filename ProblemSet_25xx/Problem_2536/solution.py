from typing import List


class Solution:
  def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
    diff = [[0] * (n+1) for _ in range(n+1)]
    
    for row1, col1, row2, col2 in queries:
      diff[row1][col1] += 1
      diff[row1][col2+1] -= 1
      diff[row2+1][col1] -= 1
      diff[row2+1][col2+1] += 1
      
    result = [[0] * n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        curr = 0
        if (j  > 0):
          curr += result[i][j-1]
        if (i  > 0):
          curr += result[i-1][j]
        if (j > 0 and i > 0):
          curr -= result[i-1][j-1]
        result[i][j] = curr + diff[i][j]
    
    return result
  
s = Solution()
result1 = s.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]])
print("Result")
for row in result1:
  print(row)
