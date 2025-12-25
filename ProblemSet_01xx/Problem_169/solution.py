from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_event = None
        maj_count = 0
        for num in nums:
            if (num == maj_event):
                maj_count += 1
            elif(maj_count > 0):
                maj_count -= 1
            else:
                maj_count = 1
                maj_event = num
        return maj_event