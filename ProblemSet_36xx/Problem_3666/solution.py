class Solution:
    def minOperations(self, s: str, k: int) -> int:
        length, count1 = len(s), s.count("1")
        state = count1 % 2
        
        def intersect(range1_high: int, range1_low: int, range2_high: int, range2_low: int) -> bool:
            if (range2_high >= range1_low and range2_low <= range1_high):
                return True
            return False
        
        def findMaximum(maximum: int, minimum: int, length: int, k: int) -> int:
            result_from_max = maximum + k if maximum + k <= length else length - (maximum + k - length)
            result_from_min = minimum + k if minimum + k <= length else length - (minimum + k - length)
            
            max_value = length if (result_from_max & 1 == length & 1) else length - 1
            max_value_low = max_value - k if (k <= max_value) else k - max_value
            max_value_high = max_value + k if max_value + k <= length else length - (max_value + k - length)
            if (intersect(maximum, minimum, max_value_high, max_value_low)):
                return max_value
            else:
                return max(result_from_max, result_from_min)
            
        def findMinimum(maximum: int, minimum: int, length: int, k: int) -> int:
            result_from_min = minimum - k if minimum - k >= 0 else k - minimum
            result_from_max = maximum - k if maximum - k >= 0 else k - maximum

            min_value = 0 if (result_from_min & 1 == 0) else 1

            min_value_low = min_value - k if k <= min_value else k - min_value
            min_value_high = min_value + k if min_value + k <= length else length - (min_value + k - length)

            if intersect(maximum, minimum, min_value_high, min_value_low):
                return min_value
            else:
                return min(result_from_max, result_from_min)
                
        minimum, maximum = count1, count1
        step = 0
        if (maximum == length):
            return step
        while step < length + 1:
            step += 1
            minimum, maximum = findMinimum(maximum, minimum, length, k), findMaximum(maximum, minimum, length, k)
            # print(step, minimum, maximum)
            if (maximum == length):
                return step
        return -1
    
s = Solution()
# print("Result", s.minOperations("110", 1))
# print("Result", s.minOperations("0001", 1))
# print("Result", s.minOperations("0101", 3))
# print("Result", s.minOperations("101", 2))
# print("Result", s.minOperations("0", 1))
# print("Result", s.minOperations("1", 1))
# print("Result", s.minOperations("01000", 3))
print("Result", s.minOperations("000000", 5))
# 0 -> (5, 5) -> (2, 0) -> (5, 3) -> (4, 0) -> (5, 1)  -> (6, 0)    
