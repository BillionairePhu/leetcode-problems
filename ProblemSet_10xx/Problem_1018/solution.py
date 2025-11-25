from typing import List


class Solution:
  def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
    curr_num, result = 0, []
    for num in nums:
      curr_num += num
      result.append(curr_num % 5 == 0)
      curr_num <<= 1
      curr_num %= 5
    return result