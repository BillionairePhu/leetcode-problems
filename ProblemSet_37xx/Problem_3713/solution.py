from typing import Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        def longestSubstringLength(freqs: Counter):
            result = 0
            prev = None
            for value in freqs.values():
                if (prev != None and value != prev):
                    return 0
                prev = value
                result += value
            return result
        
        ans = 0
        for i in range(len(s)):
            freqs = Counter()
            for j in range(i, len(s)):
                freqs[s[j]] += 1
                ans = max(ans, longestSubstringLength(freqs))
        return ans
    
s = Solution()
print("Result", s.longestBalanced("abbac"))
print("Result", s.longestBalanced("zzabccy"))
print("Result", s.longestBalanced("aba"))