class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bitString = bin(n)[2:]
        result = 0
        for char in bitString:
            result <<= 1
            result += not int(char)
        return result
    
s = Solution()
print("Result", s.bitwiseComplement(5))
print("Result", s.bitwiseComplement(7))
print("Result", s.bitwiseComplement(10))