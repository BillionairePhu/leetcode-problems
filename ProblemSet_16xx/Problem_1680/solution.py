class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo_const = 10**9 + 7
        result = 0
        for num in range(1, n+1):
            bitString = bin(num)
            result = ((result << (len(bitString)-2)) + num) % modulo_const
        return result
    
s = Solution()
print("Result", s.concatenatedBinary(1))
print("Result", s.concatenatedBinary(3))
print("Result", s.concatenatedBinary(12))
print("Result", s.concatenatedBinary(67200))
                