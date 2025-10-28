from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last_count, result = bank[0].count('1'), 0
        for i in range(1, len(bank)):
            curr_count = bank[i].count('1')
            result += curr_count * last_count
            last_count = curr_count if curr_count != 0 else last_count
        return result

s = Solution()
print("Res", s.numberOfBeams(["011001","000000","010100","001000"]))
            