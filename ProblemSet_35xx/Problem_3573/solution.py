from typing import List


class Solution:
  def maximumProfit(self, prices: List[int], k: int) -> int:
    dp_prev = [[0,0,0] for i in range(len(prices))]
    dp_curr = [[0,0,0] for i in range(len(prices))]
    for _ in range(1,k+1):
      for b in range(1, len(prices)):
        dp_curr[b][0] = dp_curr[b-1][0] + (prices[b] - prices[b-1])
        dp_curr[b][1] = dp_curr[b-1][1] + (prices[b-1] - prices[b])
        if (b >= 2):
          # Ending at the current price long
          dp_curr[b][0] = max(dp_curr[b-1][0], dp_prev[b-2][2]) + (prices[b] - prices[b-1])
          # Ending at the current price short
          dp_curr[b][1] = max(dp_curr[b-1][1], dp_prev[b-2][2]) + (prices[b-1] - prices[b])
        # Best up until the current price
        dp_curr[b][2] = max(dp_curr[b][0], dp_curr[b][1], dp_curr[b-1][2])
      dp_prev = dp_curr
      dp_curr = [[0,0,0] for _ in range(len(prices))]
      
    return dp_prev[-1][2]

s = Solution()
# print("Result", s.maximumProfit([1,7,9,8,2], 2))
print("Result", s.maximumProfit([12,16,19,19,8,1,19,13,9], 3))
# print("Result", s.maximumProfit([14,6], 1))