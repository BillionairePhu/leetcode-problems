from math import comb
from typing import List


class Solution:
  def triangularSum(self, nums: List[int]) -> int:
    result = 0
    n = len(nums) - 1
    for i, num in enumerate(nums):
      result += (num * comb(n, i)) % 10
      
    return result % 10