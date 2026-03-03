class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if (n == 1):
            return "0"
        
        middle = 2**(n-1)
        if (k == middle):
            return "1"
        else:
            inverted = k > middle
            if (inverted):
                value = self.findKthBit(n-1, middle - (k - middle))
                return "0" if value == "1" else "1"
            else:
                return self.findKthBit(n-1, k)

s = Solution()
print(s.findKthBit(3, 1))
print(s.findKthBit(4, 11))