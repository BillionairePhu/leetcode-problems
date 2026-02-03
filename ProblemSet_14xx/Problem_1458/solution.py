from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def process(index1, index2) -> int:
            processing_array = []
            if (index1 > 0):
                processing_array.append(process(index1 - 1, index2))
            if (index2 > 0):
                processing_array.append(process(index1, index2 - 1))
            if (index1 > 0 and index2 > 0):
                processing_array.append(max(process(index1 - 1, index2 - 1), 0) + nums1[index1] * nums2[index2])
            else:
                processing_array.append(nums1[index1] * nums2[index2])
            return max(processing_array)
        return process(len(nums1)-1, len(nums2)-1)
    
s = Solution()
# print("Result", s.maxDotProduct([2,1,-2,5], [3,0,-6]))
# print("Result", s.maxDotProduct([3,-2], [2,-6,7]))
print("Result", s.maxDotProduct([-1,-1], [1,1]))
print("Result", s.maxDotProduct([-3,-8,3,-10,1,3,9], [9,2,3,7,-9,1,-8,5,-1,-1]))