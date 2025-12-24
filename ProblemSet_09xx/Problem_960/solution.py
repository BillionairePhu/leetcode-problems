from typing import List


class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    dp = [1] * len(strs[0])
    for i in range(len(strs[0])):
      for j in range(i):
        is_valid = True
        for k in range(len(strs)):
          if (strs[k][i] < strs[k][j]):
            is_valid = False
            break
        if (is_valid):
          dp[i] = max(dp[i], dp[j] + 1)
    return len(strs[0]) - max(dp)
          