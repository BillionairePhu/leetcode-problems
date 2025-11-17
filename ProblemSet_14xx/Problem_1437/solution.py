from math import inf
from typing import List


class Solution:
  def kLengthApart(self, nums: List[int], k: int) -> bool:
    distance = inf
    for num in nums:
      if (num == 1):
        if (distance >= k):
          distance = 0
        else:
          return False
      else:
        distance += 1
    return True