from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def first_fruit_at_or_after_x(fruits, x):
            left, right = 0, len(fruits)  # right is exclusive
            while left < right:
                mid = (left + right) // 2
                if fruits[mid][0] < x:
                    left = mid + 1
                else:
                    right = mid
            return left if left < len(fruits) else -1

        prefixSum, sum = [], 0
        fruit_index = first_fruit_at_or_after_x(fruits, startPos - k if startPos - k > 0 else 0)
        for i in range(startPos - k, startPos + k + 1):
            if (fruit_index < len(fruits) and fruits[fruit_index][0] == i):
                sum += fruits[fruit_index][1]
                prefixSum.append(sum)
                fruit_index += 1
            else:
                prefixSum.append(sum)
                
        result = 0
        for i in range(startPos - k, startPos + k + 1):
            if (abs(i - startPos) > k):
                continue
            
            temp = self.fruitsInBetween(i, startPos, prefixSum, startPos - k)
            remaining_steps = k - 2 * abs(startPos - i)
            if (remaining_steps > 0):
                if (i <= startPos):
                    temp = self.fruitsInBetween(i, startPos + remaining_steps, prefixSum, startPos - k)
                else:
                    temp = self.fruitsInBetween(startPos - remaining_steps, i, prefixSum, startPos - k)
            if (temp > result):
                result = temp
        return result
    
    def fruitsInBetween(self, index1: int, index2: int, prefixSum: list[int], padding: int) -> int:
        index1 -= padding
        index2 -= padding
        start = min(index1, index2)
        end = max(index1, index2)
        lowerValue = 0 if start <= 0 else prefixSum[start-1]
        upperValue = prefixSum[-1] if end >= len(prefixSum) else prefixSum[end]
        return upperValue - lowerValue
        
s = Solution()
print("Result", s.maxTotalFruits([[2,8],[6,3],[8,6]], 5, 4))
print("Result", s.maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4))
print("Result", s.maxTotalFruits([[0,3],[6,4],[8,5]], 3, 2))
print("Result", s.maxTotalFruits([[200000,10000]], 200000, 10000))