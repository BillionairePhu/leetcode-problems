# Write your solution here
class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]):
        n = len(fruits)
        
        # First child at 0, 0
        first_child = 0
        for i in range(n):
            first_child += fruits[i][i]
            fruits[i][i] = 0
            
        # Second child at 0, n-1
        result = [fruits[0][n-1]]
        for i in range(1,n):
            new_result = []
            for j in range(0, i+1):
                start = max(j-1, 0)
                end = min(j+1, len(result))
                new_result.append(max(result[start:end+1]) + fruits[i][n-1-j])
            result = new_result
        second_child = result[0]
        
        # Third child at n-1, 0
        result = [fruits[n-1][0]]
        for j in range(1,n):
            new_result = []
            for i in range(0, j+1):
                start = max(i-1, 0)
                end = min(i+1, len(result))
                new_result.append(max(result[start:end+1]) + fruits[n-1-i][j])
            result = new_result
        third_child = result[0]
        
        return first_child + second_child + third_child
            
s = Solution()
print("Result", s.maxCollectedFruits([[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]))