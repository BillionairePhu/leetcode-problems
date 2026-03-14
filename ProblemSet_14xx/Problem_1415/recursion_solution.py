"""
Solution using recursion
O(3*2^(n-1))
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        shared_array = []
        count = 0
        index = k
        
        def recurse(n: int, curr: int):
            nonlocal count
            nonlocal index
            if (n == curr):
                count += 1
                if (count == k):
                    return True
                else:
                    return False
            for char in "abc":
                if (shared_array and shared_array[-1] == char):
                    continue
                shared_array.append(char)
                result = recurse(n, curr + 1)
                if (result == True):
                    return True
                shared_array.pop()
            return False
        
        final_result = recurse(n, 0)
        return "".join(shared_array) if final_result == True else ""
            
s = Solution()
print("Result", s.getHappyString(3, 9))
print("Result", s.getHappyString(1, 4))
print("Result", s.getHappyString(1, 3))