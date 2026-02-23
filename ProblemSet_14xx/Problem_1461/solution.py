class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        count, num = 0, 0
        masked = 2**(k-1) - 1
        num_set = set()
        for char in s:
            count += 1
            if (count < k):
                num = (num << 1) + int(char)
            else:
                num = ((num & masked) << 1) + int(char)
                num_set.add(num)
        return len(num_set) == 2**k
    
s = Solution()
# print("Result", s.hasAllCodes("00110110", 2))
# print("Result", s.hasAllCodes("0110", 1))
# print("Result", s.hasAllCodes("0110", 2))
print("Result", s.hasAllCodes("101000100011111001110010", 3))