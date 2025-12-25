from bisect import bisect_left
from math import sqrt


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        zeros = []
        for i in range(len(s)):
            if (s[i] == "0"):
                zeros.append(i)
        
        for i in range(len(s)):
            zero_count = 0
            index = bisect_left(zeros, i)
            while zero_count < sqrt(len(s)) and index < len(zeros):
                last_index = i if zero_count == 0 else zeros[index-1]
                must_index = i + zero_count + zero_count**2 - 1
                if (zeros[index] >= must_index):
                    result += (zeros[index] - max(must_index, last_index))
                zero_count += 1
                index += 1
            
            last_index = i if zero_count == 0 else zeros[index-1]
            must_index = i + zero_count + zero_count**2 - 1
            if (len(s) >= must_index):
                result += (len(s) - max(must_index, last_index))
            
        return result
    
s = Solution()
# print("Result", s.numberOfSubstrings("00011"))
# print("Result", s.numberOfSubstrings("101101"))
print("Result", s.numberOfSubstrings("101101"))
