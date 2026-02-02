from math import inf
from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        first_num = nums[0]
        sortedList = SortedList()
        result = inf
        minSum = inf
        for i in range(1, len(nums)):
            if (i == 1):
                for j in range(2, min(dist+2, len(nums))):
                    sortedList.add(nums[j])
                minSum = sum(sortedList[:k-2])
            else:
                if (sortedList.index(nums[i]) < k-2):
                    minSum -= nums[i]
                    if (len(sortedList) > k-2):
                        minSum += sortedList[k-2]
                sortedList.remove(nums[i])
                
                if (i + dist < len(nums)):
                    sortedList.add(nums[i + dist])
                    if (sortedList.index(nums[i + dist]) < k-2):
                        minSum += nums[i + dist]
                        if (len(sortedList) > k-2):
                            minSum -= sortedList[k-2]
                            
            if (len(sortedList) >= k-2):
                result = min(result, first_num + nums[i] + minSum)
        return result
    
s = Solution()
print("Result", s.minimumCost([1,3,2,6,4,2], 3, 3))
print("Result", s.minimumCost([10,1,2,2,2,1], 4, 3))
print("Result", s.minimumCost([10,8,18,9], 3, 1))
                