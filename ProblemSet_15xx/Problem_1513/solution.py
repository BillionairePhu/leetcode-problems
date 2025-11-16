class Solution:
    def numSub(self, s: str) -> int:
        result = 0
        consec1 = 0
        for char in s:
            if (char == "1"):
                consec1 += 1
                result += consec1
            else:
                consec1 = 0
        return result % (10**9 + 7)