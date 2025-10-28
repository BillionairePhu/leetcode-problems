from bisect import bisect_left, bisect_right
from typing import Counter, List


class Solution:
  def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
    freqs = Counter(nums)
    keys, result = list(freqs.keys()), 0
    keys.sort()
    
    index_dict, prefixes = {}, [0]
    for key in keys:
      index_dict[key] = len(prefixes)
      prefixes.append(freqs[key] + prefixes[-1])
      
    def freq_of_value_after_operations(value: int) -> int:
      lower, upper = value - k, value + k
      
      if (value in index_dict):
        value_index = index_dict[value]
        value_freq = prefixes[value_index] - prefixes[value_index-1]
      else:
        value_freq = 0
        
      lower_prefix_index = bisect_left(keys, lower)
      upper_prefix_index = bisect_right(keys, upper)
      total_freq = prefixes[upper_prefix_index] - prefixes[lower_prefix_index]
      ans = min(value_freq+numOperations, total_freq)
      return ans
      
      
    for i in range(len(keys)):
      value = keys[i]
      result = max(result, freq_of_value_after_operations(value-k))
      result = max(result, freq_of_value_after_operations(value))
    return result
      
s = Solution()
# print("Result", s.maxFrequency([1,4,5], 1, 2))
# print("Result", s.maxFrequency([69,12,107,102,89], 9, 5))
print("Result", s.maxFrequency([5,11,20,20], 5, 1))