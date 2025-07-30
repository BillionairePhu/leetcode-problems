# Write your solution here
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        max_len, curr_max_len = 0, 0
        for num in nums:
            if (num == max_value):
                curr_max_len += 1
                if (curr_max_len > max_len):
                    max_len = curr_max_len
            else:
                curr_max_len = 0
        return max_len
        