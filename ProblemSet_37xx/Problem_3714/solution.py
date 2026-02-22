class Solution:
    def longestBalanced(self, s: str) -> int:
        countABC = [0, 0, 0]
        appearancesABC = {}
        appearancesABC[(0,0,0)] = -1
        
        countAB, countBC, countAC = [0, 0], [0, 0], [0, 0]
        appearancesAB, appearancesBC, appearancesAC = {}, {}, {}
        appearancesAB[(0,0)] = -1
        appearancesBC[(0,0)] = -1
        appearancesAC[(0,0)] = -1
        
        consecutiveCount = 0
        
        result = 0
        
        def normalize(nums: list):
            minNum = min(nums)
            return tuple([num - minNum for num in nums])
        
        for index, char in enumerate(s):
            # Take into account of substring with exactly 1 type of characters
            if (index > 0 and s[index] == s[index-1]):
                consecutiveCount += 1
            else:
                consecutiveCount = 1
            result = max(result, consecutiveCount)
            
            # Increment current counts
            if (char == "c"):
                countBC[1] += 1
                countAC[1] += 1
                countABC[2] += 1
            if (char == "b"):
                countAB[1] += 1
                countBC[0] += 1
                countABC[1] += 1
            if (char == "a"):
                countAB[0] += 1
                countAC[0] += 1
                countABC[0] += 1
            
            # Take into account of substring with exactly 2 types of characters (a and b, b and c, a and c)
            if (char == "c"):
                countAB = [0,0]
                appearancesAB.clear()
                appearancesAB[(0, 0)] = index
            else:
                normalizedAB = normalize(countAB)
                appearancesAB[normalizedAB] = index if normalizedAB not in appearancesAB else appearancesAB[normalizedAB]
                result = max(result, index - appearancesAB[normalizedAB])
            
            if (char == "b"):
                countAC = [0,0]
                appearancesAC.clear()
                appearancesAC[(0, 0)] = index
            else:
                normalizedAC = normalize(countAC)
                appearancesAC[normalizedAC] = index if normalizedAC not in appearancesAC else appearancesAC[normalizedAC]
                result = max(result, index - appearancesAC[normalizedAC])
            
            if (char == "a"):
                countBC = [0,0]
                appearancesBC.clear()
                appearancesBC[(0, 0)] = index
            else:
                normalizedBC = normalize(countBC)
                appearancesBC[normalizedBC] = index if normalizedBC not in appearancesBC else appearancesBC[normalizedBC]
                result = max(result, index - appearancesBC[normalizedBC])
            
            # Take into account substring of exactly 3 types of characters
            normalizedABC = normalize(countABC)
            appearancesABC[normalizedABC] = index if normalizedABC not in appearancesABC else appearancesABC[normalizedABC]
            result = max(result, index - appearancesABC[normalizedABC])
        return result
    
s = Solution()
print("Result", s.longestBalanced("abbac"))
print("Result", s.longestBalanced("aabcc"))
print("Result", s.longestBalanced("aba"))