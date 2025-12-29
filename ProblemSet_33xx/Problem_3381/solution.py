from math import inf
from typing import List


class Solution:
  def maxSubarraySum(self, nums: List[int], k: int) -> int:
    curr_sum = sum(nums[:k])
    modulo_sums = [-1] * k
    result = -inf
    
    for index in range(k-1, len(nums)):
        result = max(result, curr_sum)
        
        if (modulo_sums[index % k] > 0):
            result = max(result, curr_sum + modulo_sums[index % k])
            modulo_sums[index % k] += curr_sum
        else:
            modulo_sums[index % k] = curr_sum
        
        if (index+1 >= len(nums)):
            break
        curr_sum += nums[index+1]
        curr_sum -= nums[index+1-k]        
    return result
        
s = Solution()
# print("Result", s.maxSubarraySum([-1,-2,-3,-4,-5], 4))
print("Result", s.maxSubarraySum([-5,1,2,-3,4], 2))
# print("Result", s.maxSubarraySum([-1,-2,-3,-4,-5], 4))
# print("Result", s.maxSubarraySum([-1,-2,-3,-4,-5], 4))