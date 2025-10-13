from typing import Counter, List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        counters = [Counter(word) for word in words]
        result = []
        
        for i in range(len(counters)):
            if (i > 0 and counters[i] == counters[i-1]):
                continue
            result.append(words[i])
        return result
    
s = Solution()
print(s.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
