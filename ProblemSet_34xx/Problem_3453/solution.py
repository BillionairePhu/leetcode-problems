from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        def area_under(limit: float) -> float:
            result = 0
            for x, y, size in squares:
                if (y < limit):
                    result += (min(limit, y + size) - y) * size
            return result
        
        low = squares[0][1]
        high = squares[0][1] + squares[0][2]
        for x, y, size in squares:
            high = max(high, y + size)
            low = min(low, y)
            total_area += size * size

        while high - low > 0.000001:
            mid = (low + high) / 2
            if (area_under(mid) >= total_area/2):
                high = mid
            else:
                low = mid
        
        return high
        
        # return exact if cover_exact else under_boundary
    
s = Solution()
# print("Result", s.separateSquares([[0,0,1],[2,2,1]]))
# print("Result", s.separateSquares([[0,0,2],[1,1,1]]))
print("Result", s.separateSquares([[2,5,3],[8,12,4]]))
        