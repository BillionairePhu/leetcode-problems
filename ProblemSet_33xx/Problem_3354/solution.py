from typing import List


class Solution:
    def isValid(self, arrays: list[int], index: int, dir: bool) -> bool:
        # print(index, dir)
        while (index < len(arrays) and index >= 0):
            if (arrays[index] != 0):
                dir = not dir
                arrays[index] -= 1
            index += (1 if dir else -1)
        # print(arrays)
        return arrays.count(0) == len(arrays)
        
    def countValidSelections(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                continue
            if (self.isValid(nums.copy(), i, False)):
                result += 1
            if (self.isValid(nums.copy(), i, True)):
                result += 1
        return result
    
s = Solution()
print("Result", s.countValidSelections([1,0,2,0,3]))