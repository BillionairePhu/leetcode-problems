class Solution:
    def numOfSubsequences(self, s: str) -> int:
        L_count, LC_count, LCT_count = 1, 0, 0
        T_count = 0
        
        # Case 1: add L to the beginning
        for char in s:
            if (char == "L"):
                L_count += 1
            elif (char == "C"):
                LC_count += L_count
            elif (char == "T"):
                LCT_count += LC_count
                T_count += 1
        res1 = LCT_count
        
        # Case 2: add T to the ending
        L_count, LC_count, LCT_count = 0, 0, 0
        for char in s:
            if (char == "L"):
                L_count += 1
            elif (char == "C"):
                LC_count += L_count
            elif (char == "T"):
                LCT_count += LC_count
        res2 = LCT_count + LC_count
        
        # Case 3: try to add C after every L
        res3 = LCT_count
        current_L_count, current_T_count = 0, 0
        for char in s:
            if (char == "L"):
                current_L_count += 1
                res3 = max(res3, LCT_count + current_L_count * (T_count - current_T_count))
            if (char == "T"):
                current_T_count += 1
        
        return max(res1, res2, res3)

s = Solution()
print('Result', s.numOfSubsequences("LT"))