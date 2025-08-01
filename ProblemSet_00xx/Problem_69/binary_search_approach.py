class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while (low < high):
            mid = (low + high) // 2
            if (mid * mid > x):
                high =  mid - 1
            else:
                low = mid + 1
            
        return low if low * low <= x else low - 1
    
s = Solution()
print('Result', s.mySqrt(100))
print('Result', s.mySqrt(101))
print('Result', s.mySqrt(121))
print('Result', s.mySqrt(2))