from typing import List


class Solution:
  def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height)-1
    result = min(height[right], height[left]) * (right-left)
    while left < right:
      if (height[left] < height[right]):
        left += 1
      else:
        right -= 1
      result = max(
        result,
        min(height[right], height[left]) * (right-left))
    return result
    