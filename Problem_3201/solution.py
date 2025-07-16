from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Even stack, start with even
        stack1 = []
        for num in nums:
            if (num % 2 == 0):
                stack1.append(num)
        
        # Even stack, start with odd
        stack2 = []
        for num in nums:
            if (num % 2 == 1):
                stack2.append(num)
                
        # Odd stack, start with odd
        stack3 = []
        isOdd = True
        for num in nums:
            if (isOdd and num % 2 == 1):
                stack3.append(num)
                isOdd = False
                continue
            if (not isOdd and num%2 == 0):
                stack3.append(num)
                isOdd = True
                continue
                
        # Odd stack, start with eeven
        stack4 = []
        isOdd = False
        for num in nums:
            if (isOdd and num % 2 == 1):
                stack4.append(num)
                isOdd = False
                continue
            if (not isOdd and num%2 == 0):
                stack4.append(num)
                isOdd = True
                continue
        
        return max(len(stack1), len(stack2), len(stack3), len(stack4))
    
s = Solution()
print("Result", s.maximumLength([1,2,1,1,2,1,2]))
        
        