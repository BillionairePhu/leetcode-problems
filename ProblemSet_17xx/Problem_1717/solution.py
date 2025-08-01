class Solution:
    def removeCombination(
            self, removeAb: bool, list_s: list[str], x: int, y: int
        ) -> tuple[list[str], int]:
        """
        Iterate from left to right and remove the substring (using stack):
        - `ab` if `removeAb` is True
        - `ba` if `removeAb` is False
        
        Returns: the remaining string and the additional score
        """
        stack, score = [], 0
        for char in list_s:
            if (removeAb and char == 'b' and stack and stack[-1] == 'a'):
                stack.pop()
                score += x if removeAb else y
            elif (not removeAb and char == 'a' and stack and stack[-1] == 'b'):
                stack.pop()
                score += x if removeAb else y
            else:
                stack.append(char)
        return stack, score
        
    def maximumGain(self, s: str, x: int, y: int) -> int:
        list_s = list(s)
        score = 0
        removeAb = x >= y
            
        additionalScore = -1
        while additionalScore != 0:
            additionalScore = 0
            
            list_s, a_score = self.removeCombination(removeAb, list_s, x, y)
            additionalScore += a_score
            
            removeAb = not removeAb
            
            list_s, a_score = self.removeCombination(removeAb, list_s, x, y)
            additionalScore += a_score
            
            score += additionalScore
        return score

s = Solution()
print("Result", s.maximumGain("cdbcbbaaabab", 4, 5))
print("Result", s.maximumGain("aabbaaxybbaabb", 5, 4))