from typing import List


class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    deleted_cols = 0
    for col in range(len(strs[0])):
      prev_chr = strs[0][col]
      for str_index in range(1, len(strs)):
        if (strs[str_index][col] < prev_chr):
          deleted_cols += 1
          break
        prev_chr = strs[str_index][col]
    return deleted_cols