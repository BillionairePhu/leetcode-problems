class Solution:
    def computeArea(self,
        ax1: int, ay1: int, ax2: int, ay2: int,
        bx1: int, by1: int, bx2: int, by2: int
        ) -> int:
        sq1 = (ax2 - ax1) * (ay2 - ay1)
        sq2 = (bx2 - bx1) * (by2 - by1)
        
        overlap_deltax = (min(ax2, bx2) - max(ax1, bx1))
        overlap_deltay = (min(ay2, by2) - max(ay1, by1))
        overlap = overlap_deltax * overlap_deltay
        
        return sq1 + sq2 - overlap if (overlap_deltay > 0 and overlap_deltax > 0) else sq1 + sq2
        
s = Solution()
print("Result", s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
print("Result", s.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2))
print("Result", s.computeArea(
    ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2,
    bx1 = 2, by1 = 2, bx2 = 3, by2 = 3))
print("Result", s.computeArea(
    ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2,
    bx1 = -3, by1 = -3, bx2 = -1, by2 = -1))
print("Result", s.computeArea(
    ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4,
    bx1 = 4, by1 = -1, bx2 = 9, by2 = 2))
print("Result", s.computeArea(
    ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4,
    bx1 = 4, by1 = -1, bx2 = 9, by2 = -0.5))