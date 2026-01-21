from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def solveBitwise(num: int) -> int:
            if (num % 2 == 0):
                return -1
            num_str = str(bin(num))
            
            result = []
            flag = False
            for i in range(len(num_str)-1, 1, -1):
                if (num_str[i] == "1" and flag == False and (i == 2 or  num_str[i-1] == "0")):
                    result.append("0")
                    flag = True
                else:
                    result.append(num_str[i])
            result_str = "".join(result)[::-1]
            return int(result_str, 2)
        
        return [solveBitwise(num) for num in nums]