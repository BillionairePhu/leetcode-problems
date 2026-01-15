from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()
        
        max_horizontal, max_vertical = 0, 0
        
        curr, count = 0, 0
        for hBar in hBars:
            if (hBar == curr + 1):
                count += 1
            else:
                count = 1
            curr = hBar
            max_horizontal = max(max_horizontal, count)
        
        curr, count = 0, 0
        for vBar in vBars:
            if (vBar == curr + 1):
                count += 1
            else:
                count = 1
            curr = vBar
            max_vertical = max(max_vertical, count)
        
        size = min(max_horizontal, max_vertical)
        return (size + 1) ** 2
        
s = Solution()
print("Result", s.maximizeSquareHoleArea(2, 3, [2,3], [2,4]))
