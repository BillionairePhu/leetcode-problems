from typing import List


class Solution:
  def numberOfPairs(self, points: List[List[int]]) -> int:
    x_sorted = sorted(points, key=lambda x: (-x[0],x[1]))
    result = 0
    
    for point in points:
      x, y = point
      maxi_y = None
      
      for other in x_sorted:
        if (other[0] > x or other[1] < y):
          continue
        if (other[0] == x and other[1] == y):
          continue
        if (maxi_y == None):
          maxi_y = other[1]
          result += 1
        elif (maxi_y > other[1]):
          maxi_y = other[1]
          result += 1
    
      print(point, result)
    
    return result
        
    
s = Solution()
# print(s.numberOfPairs([[6,2],[4,4],[2,6]]))
# print(s.numberOfPairs([[1,1],[2,2],[3,3]]))
print(s.numberOfPairs([[3,1],[1,3],[1,1]]))