class Solution:
    def minPartitions(self, n: str) -> int:
        result = 0
        for i in range(len(n)):
            result = max(result, int(n[i]))
        return result
    
s = Solution()
print("Result", s.minPartitions("32"))
print("Result", s.minPartitions("82734"))
print("Result", s.minPartitions("27346209830709182346"))