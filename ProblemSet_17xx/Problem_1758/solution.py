class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += 1 if (int(s[i]) == i % 2) else 0
        return min(count, len(s) - count)
    
s = Solution()
print("Result", s.minOperations("0100"))
print("Result", s.minOperations("10"))
print("Result", s.minOperations("1111"))