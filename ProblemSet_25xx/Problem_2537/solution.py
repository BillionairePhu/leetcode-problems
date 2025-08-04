# Write your solution here
import math
from typing import Counter, List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = Counter()
        result = 0
        start = 0
        comb_count = 0
        for end in range(len(nums)):
            num = nums[end]
            counter[num] += 1
            comb_count = comb_count - math.comb(counter[num]-1, 2) + math.comb(counter[num], 2)
            while comb_count >= k:
                result += (len(nums) - end)
                num = nums[start]
                comb_count = comb_count - math.comb(counter[num], 2) + math.comb(counter[num] - 1, 2)
                start += 1
                counter[num] -= 1
                    
        return result

s = Solution()
print("Result", s.countGood([3,1,4,3,2,2,4], 2))