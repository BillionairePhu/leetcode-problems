class Solution:
    def numOfWays(self, n: int) -> int:
        if (n == 1):
            return 12
        two_color_count = 6
        three_color_count = 6
        modulo_const = 10**9 + 7
        
        for _ in range(n-1):
            new_two_color_count = two_color_count * 3 + three_color_count * 2
            new_three_color_count = two_color_count * 2 + three_color_count * 2
            two_color_count = new_two_color_count % modulo_const
            three_color_count = new_three_color_count % modulo_const
        
        return (two_color_count + three_color_count) % modulo_const
        
s = Solution()
# print(s.numOfWays(1))
print(s.numOfWays(5000))