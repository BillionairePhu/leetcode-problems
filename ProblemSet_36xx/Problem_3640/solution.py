from math import inf
from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        valueStack = []
        signStack = []
        edgeStack = []
        increaseStack = []
        result = -inf
        for index in range(1, len(nums)):
            if (nums[index] == nums[index-1]):
                valueStack.append(0)
                signStack.append(0)
                edgeStack.append(nums[index-1])
            elif (nums[index] > nums[index-1]):
                if (signStack and signStack[-1] == 1):
                    valueStack[-1] += nums[index]
                    increaseStack[-1] = max(increaseStack[-1] + nums[index], nums[index] + nums[index-1])
                else:
                    valueStack.append(nums[index] + nums[index-1])
                    increaseStack.append(nums[index] + nums[index-1])
                    signStack.append(1)
                    edgeStack.append(nums[index-1])
                if (len(signStack) >= 3 and signStack[-2] == -1 and signStack[-3] == 1):
                    result = max(
                        result,
                        valueStack[-1] + valueStack[-2] + valueStack[-3] - edgeStack[-1] - edgeStack[-2])
                    # print("Update", valueStack[-1] + valueStack[-2] + valueStack[-3] - edgeStack[-1] - edgeStack[-2])
            else:
                if (signStack and signStack[-1] == -1):
                    valueStack[-1] += nums[index]
                else:
                    valueStack.append(nums[index] + nums[index-1])
                    signStack.append(-1)
                    edgeStack.append(nums[index-1])
                    if (len(signStack) >= 2 and signStack[-2] == 1):
                        valueStack[-2] = max(valueStack[-2], increaseStack[-1])
            print(nums[index], valueStack, edgeStack, signStack, result, increaseStack)
        return result
    
s = Solution()
# print("Result", s.maxSumTrionic([0,-2,-1,-3,0,2,-1]))
# print("Result", s.maxSumTrionic([1,4,2,7]))
# print("Result", s.maxSumTrionic([0,-3,-2,-1,-3,0,2,-1]))
print("Result", s.maxSumTrionic([286,528,-900,327,536,625,547,997]))