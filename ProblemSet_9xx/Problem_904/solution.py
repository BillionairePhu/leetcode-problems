# Write your solution here
from collections import deque
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0
        option1, option2 = set(), set()
        option1Res, option2Res = 0, 0
        
        def updateOption(fruit: int, option: set, other_option: set, optionRes: int):
            if (fruit in option):
                optionRes += 1
            elif (len(option) < 2):
                option.add(fruit)
                if (option != other_option):
                    optionRes += 1
                else:
                    option.clear()
                    option.add(fruit)
                    optionRes = 1
            else:
                option.clear()
                option.add(fruit)
                optionRes = 1
            return optionRes
        
        for fruit in fruits:
            option1Res = updateOption(fruit, option1, option2, option1Res)
            if not (len(option1) == 1 and len(option2) == 0):
                option2Res = updateOption(fruit, option2, option1, option2Res)
            result = max(result, option1Res, option2Res)
        return result
    
s = Solution()
# print("Result", s.totalFruit([0,1,2,2]))
print("Result", s.totalFruit([1,0,1,4,1,4,1,2,3]))
                