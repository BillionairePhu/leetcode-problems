import copy
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], n: int, m: int) -> int:
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for word in strs:
            new_dp = copy.deepcopy(dp)
            num_0 = word.count("0")
            num_1 = len(word) - num_0
            for i in range(n+1):
                for j in range(m+1):
                    if (i > 0):
                        new_dp[i][j] = max(new_dp[i][j], new_dp[i-1][j])
                    if (j > 0):
                        new_dp[i][j] = max(new_dp[i][j], new_dp[i][j-1])
                    
                    prev_0 = i - num_0
                    prev_1 = j - num_1
                    if (prev_0 >= 0 and prev_1 >= 0):
                        new_dp[i][j] = max(dp[prev_0][prev_1] + 1, new_dp[i][j])
            dp = new_dp
                    
        return dp[-1][-1]

s = Solution()
print("Result", s.findMaxForm(["10","0001","111001","1","0"], 5, 3))