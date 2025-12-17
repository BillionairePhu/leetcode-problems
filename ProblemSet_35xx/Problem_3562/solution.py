from typing import List


class Solution:
  def maxProfit(self, n: int,
    present: List[int], future: List[int],
    hierarchy: List[List[int]],
    budget: int,
  ) -> int:
    g = [[] for _ in range(n)]
    for boss, sub in hierarchy:
      g[boss - 1].append(sub - 1)

    def dfs(u: int):
      cost = present[u]
      dCost = present[u] // 2
      uSize = cost

      # dp[u][state][budget]
      # state = 0: Do not purchase parent node, state = 1: Must purchase parent node
      dp0 = [0] * (budget + 1)
      dp1 = [0] * (budget + 1)

      # subProfit[state][budget]
      # state = 0: discount not available, state = 1: discount available
      subProfit0 = [0] * (budget + 1)
      subProfit1 = [0] * (budget + 1)

      for v in g[u]:
        child_dp0, child_dp1, vSize = dfs(v)
        uSize += vSize
        for i in range(budget, -1, -1):
          for sub in range(min(vSize, i) + 1):
            if i - sub >= 0:
              subProfit0[i] = max(
                subProfit0[i],
                subProfit0[i - sub] + child_dp0[sub],
              )
              subProfit1[i] = max(
                subProfit1[i],
                subProfit1[i - sub] + child_dp1[sub],
              )

      for i in range(budget + 1):
        dp0[i] = subProfit0[i]
        dp1[i] = subProfit0[i]
        if i >= dCost:
          dp1[i] = max(
            subProfit0[i], subProfit1[i - dCost] + future[u] - dCost
          )
        if i >= cost:
          dp0[i] = max(
            subProfit0[i], subProfit1[i - cost] + future[u] - cost
          )

      return dp0, dp1, uSize

    return dfs(0)[0][budget]