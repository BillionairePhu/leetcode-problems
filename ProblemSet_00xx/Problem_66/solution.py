from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remember = False
        for i in range(len(digits)-1, -1, -1):
            if (i == len(digits)-1):
                digits[i] += 1
            if (remember):
                digits[i] += 1
                remember = False
                
            if (digits[i] >= 10):
                digits[i] = digits[i] % 10
                remember = True
                if (i == 0):
                    digits.insert(0, 1)
        return digits
    
s = Solution()
print("Result", s.plusOne([9,9]))
print("Result", s.plusOne([1, 9, 9]))
print("Result", s.plusOne([3, 5, 9, 9]))