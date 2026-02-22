class Solution:
    def binaryGap(self, n: int) -> int:
        last_one_index, result = -1, 0
        
        # Index of the current number starting from the right
        index = 0
        while n > 0:
            if (n & 1 == 1):
                if (last_one_index != -1):
                    result = max(result, index - last_one_index)
                last_one_index = index
            index += 1
            n >>= 1
            
        return result
    
s = Solution()
# 10110
print("Result", s.binaryGap(22))
# 1000
print("Result", s.binaryGap(8))
# 101
print("Result", s.binaryGap(5))
# 111
print("Result", s.binaryGap(7))
print("Result", s.binaryGap(int("100100001",2)))