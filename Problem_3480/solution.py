# Write your solution here
from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(n+1)]
        for pair in conflictingPairs:
            right[max(pair)].append(min(pair))
            
        tops = [0, 0]
        score = 0
        bonus = [0] * (n+1)
        for i in range(1, n+1):
            for value in right[i]:
                if (value > tops[0]):
                    tops[1] = tops[0]
                    tops[0] = value
                elif (value > tops[1]):
                    tops[1] = value
            score += i - tops[0]
            
            if (tops[0] > 0):
                bonus[tops[0]] += tops[0] - tops[1]
            
        return score + max(bonus)