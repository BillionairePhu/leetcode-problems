"""
Solution using ternary iteration, a.k.a brute forcing.
O(3^n)
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def checkIfTernaryIsHappy(n: int, num: int) -> bool:
            lastDigit = -1
            for i in range(n):
                digit = num % 3
                if (digit == lastDigit):
                    return False
                lastDigit = digit
                num //= 3
            return True
        
        def turnTernaryToString(n: int, num: int) -> str:
            letters = "abc"
            array = []
            for i in range(n):
                digit = num % 3
                array.append(letters[digit])
                num //= 3
            return "".join(array[::-1])
        
        count = 0
        for i in range(3**n):
            if (checkIfTernaryIsHappy(n, i)):
                count += 1
                print(i)
                if (count == k):
                    return turnTernaryToString(n, i) 
        return ""
    
s = Solution()
print("Result", s.getHappyString(1, 3))
print("Result", s.getHappyString(1, 4))
print("Result", s.getHappyString(3, 9))