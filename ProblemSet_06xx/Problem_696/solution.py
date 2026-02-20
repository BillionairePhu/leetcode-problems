class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr, currCount = "0", 0
        prevCount = 0
        result = 0
        
        for char in s:
            if (char == curr):
                currCount += 1
            else:
                prevCount = currCount
                curr = char
                currCount = 1
                
            if prevCount >= currCount:
                result += 1
        
        return result
    
s = Solution()
print("Result", s.countBinarySubstrings("00110011"))
print("Result", s.countBinarySubstrings("10101"))