import bisect
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect_right(letters, target)
        if (index >= len(letters)):
            return letters[0]
        else:
            return letters[index]
        
s = Solution()
print("Result", s.nextGreatestLetter(["c","f","j"], "a"))
print("Result", s.nextGreatestLetter(["c","f","j"], "c"))