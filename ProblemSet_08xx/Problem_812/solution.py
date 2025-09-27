from typing import List


class Solution:
  def largestTriangleArea(self, points: List[List[int]]) -> float:
    
    def triangle_area(p1, p2, p3):
      """
      Calculate the area of a triangle given its three vertices in 2D.
      Each point is a tuple (x, y).
      """
      x1, y1 = p1
      x2, y2 = p2
      x3, y3 = p3

      # Shoelace formula
      area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
      return area
    result = 0
    for i in range(len(points)-2):
      for j in range(i+1, len(points)-1):
        for k in range(j+1, len(points)):
          result = max(result, triangle_area(points[i], points[j], points[k]))
          
    return result