from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[[] for j in range(k)] for i in range(k)]
        
        for num in nums:
            modulo = num % k
            for i in range(k):
                sym_modulo = (i - modulo) % k
                if (len(dp[i][modulo]) <= 0):
                    dp[i][modulo].append(num)
                elif ((dp[i][modulo][-1] + num) % k == i):
                        dp[i][modulo].append(num) 
                        
                if (sym_modulo == modulo or len(dp[i][sym_modulo]) <= 0):
                    continue
                elif ((dp[i][sym_modulo][-1] + num) % k == i):
                        dp[i][sym_modulo].append(num) 
        result = 0
        for i in range(k):
            for j in range(k):
                if (len(dp[i][j]) > result):
                    result = len(dp[i][j])
        return result
    
s = Solution()
# print('Result', s.maximumLength([1,2,3,4,5], 2))
print('Result', s.maximumLength([1,4,2,3,1,4], 3))