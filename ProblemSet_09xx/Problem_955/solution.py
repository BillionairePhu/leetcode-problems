from typing import List


class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    result = 0
    equal_prev = [True for _ in range(len(strs))]
    
    def checkColumnIfNeedDeletion(col_index: int) -> tuple[bool, list[int], bool]:
      prev_char = strs[0][col_index]
      exist_equal = False
      no_more_equal_strs = []
      for str_index in range(1, len(strs)):
        # Only need to check if the current string is equal to the prev string. Because:
        # - If it is strictly larger, any suffix added to an already-larger string is still larger
        # - If it is strictly smaller, that's impossible (our algorithm will delete any column that is not in-order)
        if (equal_prev[str_index] == True):
          if (strs[str_index][col_index] < prev_char):
            return True, [], True
          elif (strs[str_index][col_index] == prev_char):
            exist_equal = True
          else:
            no_more_equal_strs.append(str_index)
        prev_char = strs[str_index][col_index]
      return False, no_more_equal_strs, exist_equal
          
    
    for i in range(len(strs[0])):
      need_deletion, no_more_equal_strs, exist_equal = checkColumnIfNeedDeletion(i)
      if (need_deletion):
        result += 1
        continue
      for not_equal_str in no_more_equal_strs:
        equal_prev[not_equal_str] = False
      if (not exist_equal):
        break
    
    return result

s = Solution()
# print("Result", s.minDeletionSize(["ca","bb","ac"]))
# print("Result", s.minDeletionSize(["xc","yb","za"]))
# print("Result", s.minDeletionSize(["zyx","wvu","tsr"]))
# print("Result", s.minDeletionSize(["xga","xfb","yfa"]))
# print("Result", s.minDeletionSize([
#   "vdy",
#   "vei",
#   "zvc",
#   "zld"]))
print("Result", s.minDeletionSize(["doeeqiy","yabhbqe","twckqte"]))