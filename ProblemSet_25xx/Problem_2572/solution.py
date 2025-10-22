from typing import List


class Solution:
  def squareFreeSubsets(self, nums: List[int]) -> int:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    sqrs = {4, 8, 12, 16, 20, 24, 28, 9, 18, 27, 25}
    modulo_cons = 10**9 + 7
    mask_count = [0 for _ in range(2**10)]
    
    def findMask(num: int) -> int:
      result = 0
      for prime in primes:
        if (num % prime == 0):
          result += 1
        result <<= 1
      return result >> 1
    
    for i in range(len(nums)):
      new_mask_count = [0 for _ in range(2**10)]
      curr_num_mask = findMask(nums[i])
      if (nums[i] in sqrs):
        continue
      
      # Process with mask 0
      new_mask_count[curr_num_mask] += 1
      print('i=',i,sum(new_mask_count))
      
      # Process with other mask
      for j in range(0, 2**10):
        if (j & curr_num_mask != 0):
          continue
        new_mask_count[j|curr_num_mask] += mask_count[j]
        
      # print('i=',i,sum(new_mask_count))
      for j in range(2**10):
        new_mask_count[j] = (new_mask_count[j] + mask_count[j]) % modulo_cons
      mask_count = new_mask_count
      # print('i=',i,sum(mask_count))
    return sum(mask_count) % modulo_cons
  
s = Solution()
# print("Result", s.squareFreeSubsets([3,4,4,5]))
# print("Result", s.squareFreeSubsets([1]))
print("Result", s.squareFreeSubsets([17,27,20,1,19]))