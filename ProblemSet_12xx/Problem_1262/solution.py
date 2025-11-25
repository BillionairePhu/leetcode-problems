from typing import List


class Solution:
  def maxSumDivThree(self, nums: List[int]) -> int:
    result = 0
    two_smallest_ones = []
    two_smallest_twos = []
    for num in nums:
      result += num
      if (num % 3 == 1):
        if (len(two_smallest_ones) < 2):
          two_smallest_ones.append(num)
          two_smallest_ones.sort()
          continue
        if (num <= two_smallest_ones[1] and num <= two_smallest_ones[0]):
          two_smallest_ones[1] = two_smallest_ones[0]
          two_smallest_ones[0] = num
        elif (num <= two_smallest_ones[1] and num > two_smallest_ones[0]):
          two_smallest_ones[1] = num
      elif (num % 3 == 2):
        if (len(two_smallest_twos) < 2):
          two_smallest_twos.append(num)
          two_smallest_twos.sort()
          continue
        if (num <= two_smallest_twos[1] and num <= two_smallest_twos[0]):
          two_smallest_twos[1] = two_smallest_twos[0]
          two_smallest_twos[0] = num
        elif (num <= two_smallest_twos[1] and num > two_smallest_twos[0]):
          two_smallest_twos[1] = num
      # print(num, two_smallest_ones, two_smallest_twos)
    # print(result)
    # print(two_smallest_ones)
    # print(two_smallest_twos)
    
    if (result % 3 == 1):
      if (len(two_smallest_ones) == 0):
        result -= sum(two_smallest_twos)
      else:
        result -= min(two_smallest_ones[0], sum(two_smallest_twos)) if len(two_smallest_twos) == 2 else two_smallest_ones[0]
    elif (result % 3 == 2):
      if (len(two_smallest_twos) == 0):
        result -= sum(two_smallest_ones)
      else:
        result -= min(two_smallest_twos[0], sum(two_smallest_ones)) if len(two_smallest_ones) == 2 else two_smallest_twos[0]
    
    return result
  
s = Solution()
# print("Result", s.maxSumDivThree([3,6,5,1,8]))
print("Result", s.maxSumDivThree([4,1,5,3,1]))