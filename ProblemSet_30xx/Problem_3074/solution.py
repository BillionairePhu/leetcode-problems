import heapq
from typing import List


class Solution:
  def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
    result = 0
    apple_count = sum(apple)
    inversed_capacity = [-value for value in capacity]
    heapq.heapify(inversed_capacity)
    
    while len(inversed_capacity) > 0 and apple_count > 0:
      capac = heapq.heappop(inversed_capacity)
      apple_count += capac
      result += 1
    return result
      