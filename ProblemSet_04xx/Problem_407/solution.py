import heapq
from typing import List


class Solution:
  def trapRainWater(self, heightMap: List[List[int]]) -> int:
    m, n = len(heightMap), len(heightMap[0])
    boundary, trapping_water = [], 0
    visited = [ [False]*n for _ in range(m) ]
    directions = [ [0, -1], [0, 1], [1, 0], [-1, 0] ]
    
    # Add cells in the first and last column to the boundary heap
    for i in range(m):
      heapq.heappush(boundary, [heightMap[i][0], i, 0])
      visited[i][0] = True
      heapq.heappush(boundary, [heightMap[i][n-1], i, n-1])
      visited[i][n-1] = True
      
    # Add cells in the first and last row to the boundary heap (except the corner)
    for i in range(1, n-1):
      heapq.heappush(boundary, [heightMap[0][i], 0, i])
      visited[0][i] = True
      heapq.heappush(boundary, [heightMap[m-1][i], m-1, i])
      visited[m-1][i] = True
    
    while len(boundary) > 0:
      curr_height, curr_row, curr_col = heapq.heappop(boundary)
      
      for direction in directions:
        neighbor_row = curr_row + direction[0]
        neighbor_col = curr_col + direction[1]
        if (neighbor_row < 0 or neighbor_row >= m or neighbor_col < 0 or neighbor_col >= n):
          continue
        if (visited[neighbor_row][neighbor_col] == True):
          continue
        neighbor_height = heightMap[neighbor_row][neighbor_col]
        
        if (neighbor_height < curr_height):
          trapping_water += (curr_height - neighbor_height)
          # print(curr_row, curr_col, curr_height, neighbor_row, neighbor_col, neighbor_height)
        visited[neighbor_row][neighbor_col] = True
        heapq.heappush(boundary, [max(heightMap[neighbor_row][neighbor_col], curr_height), neighbor_row, neighbor_col])
    
    return trapping_water
  
s = Solution()
print(s.trapRainWater([
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]])) 
      