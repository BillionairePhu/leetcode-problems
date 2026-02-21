from math import inf


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        lowest, curr, temp = inf, 0, inf
        for char in s:
            if (char == "1"):
                curr += 1
                lowest = min(lowest, temp)
            else:
                curr -= 1
                temp = min(temp, curr)
        
        specialSubstrings = []
        currSubstr, currDifference = [], -lowest
        opening, alreadyOpened = [], False
        for char in s:
            if (currDifference < 0 and not alreadyOpened):
                opening.append(char)
                currDifference += 1 if char == "1" else -1
                continue
            
            currSubstr.append(char)
            alreadyOpened = True
            currDifference += 1 if char == "1" else -1
                
            if (currDifference == 0):
                currProcessedSubString = "".join(currSubstr)
                if (len(currSubstr) != len(s)):
                    currProcessedSubString = self.makeLargestSpecial(currProcessedSubString)
                    
                specialSubstrings.append(currProcessedSubString)
                currSubstr, currDifference = [], 0
        specialSubstrings.sort(reverse=True)

        # The result is the combination of
        # - The opening string
        # - The special substrings in lexicographically reversed order (we want the largests to be the firsts)
        # - The closing string (which is the remaining unprocessed string)
        return "".join(opening) + "".join(specialSubstrings) + "".join(currSubstr)
        
    
s = Solution()
# print("Result", s.makeLargestSpecial("11011000"))
# print("Result", s.makeLargestSpecial("10"))
print("Result", s.makeLargestSpecial("10110111000011100100"))