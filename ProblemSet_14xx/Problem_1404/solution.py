class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        step = 0
        
        while num != 1:
            num = num + 1 if (num & 1 == 1) else num >> 1
            step += 1
        return step
    
s = Solution()
print("Result", s.numSteps("1101"))