class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [
            [
                [0, 0] for j in range(one + 1)    
            ] for i in range(zero + 1)
        ]
        modConst = 1e9 + 7
        
        for i in range(1, min(limit, zero) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(limit, one) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                if (i <= limit):
                    dp[i][j][0] = dp[i-1][j][1] + dp[i-1][j][0]
                else:
                    dp[i][j][0] = dp[i-1][j][1] + (dp[i-1][j][0] - dp[i-limit-1][j][1])
                
                if (j <= limit):
                    dp[i][j][1] = dp[i][j-1][1] + dp[i][j-1][0]
                else:
                    dp[i][j][1] = (dp[i][j-1][1] - dp[i][j-limit-1][0]) + dp[i][j-1][0]
                    
                dp[i][j][0] = int(dp[i][j][0] % modConst)
                dp[i][j][1] = int(dp[i][j][1] % modConst)
        
        # for row in dp:
        #     print(row)
        
        return int(sum(dp[zero][one]) % modConst)

s = Solution()
# print("Result", s.numberOfStableArrays(1,1,2))  
# print("Result", s.numberOfStableArrays(1,2,1))  
# print("Result", s.numberOfStableArrays(3,3,2))  
# print("Result", s.numberOfStableArrays(1,4,2))  
# print("Result", s.numberOfStableArrays(19,15,15))  
print("Result", s.numberOfStableArrays(20,15,75))  