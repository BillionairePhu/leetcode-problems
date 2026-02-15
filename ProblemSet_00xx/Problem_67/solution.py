class Solution:
    def addBinary(self, a: str, b: str) -> str:
        numA, numB = int(a, 2), int(b, 2)
        return bin(numA + numB)[2:]
    
s = Solution()
print("Result", s.addBinary("11", "1"))
print("Result", s.addBinary("1010", "1011"))