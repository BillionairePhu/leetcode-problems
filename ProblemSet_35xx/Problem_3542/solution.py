from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result, stack = 0, []
        for num in nums:
            # print(result, len(stack))
            if (len(stack) == 0):
                if (num == 0):
                    continue
                stack.append(num)
                continue
            
            if (num > stack[-1]):
                stack.append(num)
            elif (num < stack[-1]):
                while (len(stack) > 0 and stack[-1] > num):
                    stack.pop()
                    result += 1
                if (num == 0):
                    continue
                if (len(stack)>0 and stack[-1] == num):
                    continue
                stack.append(num)
        return result + len(stack)
    
s = Solution()
print(s.minOperations([3,1,2,1]))