class Solution:
    def maxOperations(self, s: str) -> int:
        result, positions, last = 0, 0, ""
        for i in range(len(s)-1, -1, -1):
            if (s[i] == "1"):
                if (last == "0"):
                    positions += 1
                result += positions
            last = s[i]
        return result
    
s = Solution()
print(s.maxOperations("1001101"))
print(s.maxOperations("00111"))