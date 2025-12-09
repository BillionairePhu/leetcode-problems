from typing import Counter, List


class Solution:
  def specialTriplets(self, nums: List[int]) -> int:
    left_counter = Counter()
    right_counter = Counter(nums)
    result, modulo_const = 0, 10**9 + 7
    
    for num in nums:
      right_counter[num] -= 1
      result = (result + left_counter[num*2] * right_counter[num*2]) % modulo_const
      left_counter[num] += 1
    
    return result