from typing import List


class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    array_sum = sum(nums)
    target_modulo = array_sum % p
    
    if (target_modulo == 0):
      return 0
    
    closest_target_modulos = {0: -1}
    curr_sum, result = 0, len(nums)
    
    for i, num in enumerate(nums):
      curr_sum += num
      curr_modulo = curr_sum % p
      needed_modulo = (curr_modulo - target_modulo) % p
      
      if (needed_modulo in closest_target_modulos):
        result = min(result, i - closest_target_modulos[needed_modulo])
      
      closest_target_modulos[curr_modulo] = i
    
    return result if result < len(nums) else -1
  
s = Solution()
# print("Result", s.minSubarray([3,1,4,2], 6))
# print("Result", s.minSubarray([6,3,5,2], 9))
# print("Result", s.minSubarray([1,2,3], 3))
# print("Result", s.minSubarray([1], 3))
print("Result", s.minSubarray([3], 3))
# print("Result", s.minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2], 148))