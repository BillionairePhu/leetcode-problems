# Write your solution here
class Solution:
  def numberOfWays(self, n: int, x: int) -> int:
    modulo = 10**9 + 7
    items, i = [], 1
    while i**x <= n:
      items.append(i**x)
      i += 1
      
    dp = [ [-1] * (len(items)) for _ in range(n+1) ]
    
    for i in range(n+1):
      for j in range(len(items)):
        count = 0
        if (i == 0):
          dp[i][j] = 1
          continue
        
        # Case 1: not select the j-th item
        if (j > 0):
          count += dp[i][j-1]
          
        # Case 2: selecting the j-th item
        if (i - items[j] >= 0 and j > 0):
          count += dp[i-items[j]][j-1]
        elif (i - items[j] == 0 and j == 0):
          count += 1
        
        dp[i][j] = count % modulo
    
    return dp[-1][-1]
  
s = Solution()
# print("Result", s.numberOfWays(10, 2))
# print("Result", s.numberOfWays(4, 1))
print("Result", s.numberOfWays(10, 1))
    