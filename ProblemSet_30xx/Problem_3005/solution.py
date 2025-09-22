from typing import Counter, List


class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    counter = Counter(nums)
    result = 0
    max_freq = 0
    for freq in counter.values():
      if (freq > max_freq):
        max_freq = freq
        result = freq
      elif (freq == max_freq):
        result += freq
    return result