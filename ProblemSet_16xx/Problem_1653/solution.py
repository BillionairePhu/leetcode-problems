class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0
        b_count = s.count("b")
        result = b_count
        for char in s:
            if (char == "a"):
                a_count += 1
            else:
                b_count -= 1
            result = max(result, a_count + b_count)
        return len(s) - result
    
s = Solution()
print("Result", s.minimumDeletions("aababbab"))
print("Result", s.minimumDeletions("bbaaaaabb"))