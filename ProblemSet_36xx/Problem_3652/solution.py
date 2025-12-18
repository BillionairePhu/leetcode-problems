from typing import List


class Solution:
  def maxProfit(self,
      prices: List[int], strategy: List[int], k: int) -> int:
    k = k // 2
    window_profit = sum(prices[k:2*k]) \
      + sum([prices[i]*strategy[i] for i in range(2*k, len(prices))])
    max_profit = window_profit
    
    for i in range(len(prices)-k*2):
      window_profit += (prices[i]*strategy[i] - prices[i+k] + prices[i+2*k] - prices[i+2*k]*strategy[i+2*k])
      max_profit = max(max_profit, window_profit)
      
    return max(max_profit, sum([prices[i]*strategy[i] for i in range(len(prices))]))

s = Solution()
print("Result", s.maxProfit([4,2,8], [-1,0,1], 2))