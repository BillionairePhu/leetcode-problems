from typing import Counter, List


class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    counter = Counter(nums)
    max_key, max_freq = None, 0
    for key, freq in counter.items():
      if (freq > max_freq):
        max_key = key
        max_freq = freq
    return max_key