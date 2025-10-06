from typing import List


class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    pacific = [[0 for j in range(len(heights[0]))] for i in range(len(heights))]
    atlantic = [[0 for j in range(len(heights[0]))] for i in range(len(heights))]
    
    def spread(heights, i, j, matrix):
      if (matrix[i][j] == 1):
        return
      
      matrix[i][j] = 1
      
      if (i > 0 and heights[i-1][j] >= heights[i][j]):
        spread(heights, i-1, j, matrix)
      if (j > 0 and heights[i][j-1] >= heights[i][j]):
        spread(heights, i, j-1, matrix)
      if (i < len(heights)-1 and heights[i+1][j] >= heights[i][j]):
        spread(heights, i+1, j, matrix)
      if (j < len(heights[0])-1 and heights[i][j+1] >= heights[i][j]):
        spread(heights, i, j+1, matrix)
    
    # Upper cells flowing to Pacific
    for j in range(len(heights[0])):
      spread(heights, 0, j, pacific)
    # Left cells flowing to Pacific
    for i in range(len(heights)):
      spread(heights, i, 0, pacific)
    # Bottom cells flowing to Atlantic
    for j in range(len(heights[0])):
      spread(heights, len(heights)-1, j, atlantic)
    # Right cells flowing to Atlantic
    for i in range(len(heights)):
      spread(heights, i, len(heights[0])-1, atlantic)
      
    # print("Pacific")
    # for row in pacific:
    #   print(row)  
    # print("Atlantic")
    # for row in atlantic:
    #   print(row)  
    
    result = []
    for i in range(len(heights)):
      for j in range(len(heights[0])):
        if (pacific[i][j] == 1 and atlantic[i][j] == 1):
          result.append([i, j])
    return result
  
s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))