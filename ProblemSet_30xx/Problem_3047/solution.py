from typing import List


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        
        def calculate_overlapping_square(first_rect: list[int], second_rect: list[int]) -> int:
            first_bottom_left, first_top_right = first_rect
            second_bottom_left, second_top_right = second_rect
            
            overlapping_bottom_left = [
                max(first_bottom_left[0], second_bottom_left[0]),
                max(first_bottom_left[1], second_bottom_left[1])]
            overlapping_top_right = [
                min(first_top_right[0], second_top_right[0]),
                min(first_top_right[1], second_top_right[1])]
            
            width = overlapping_top_right[0] - overlapping_bottom_left[0]
            height = overlapping_top_right[1] - overlapping_bottom_left[1]
            if (width > 0 and height > 0):
                return min(width, height) ** 2
            else:
                return -1
        
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                overlapping_area = calculate_overlapping_square(
                    [bottomLeft[i], topRight[i]],
                    [bottomLeft[j], topRight[j]]
                )
                result = max(result, overlapping_area)
                print(overlapping_area)
        return result
    
s = Solution()
print("Result", s.largestSquareArea([[1,1],[1,3],[1,5]],  [[5,5],[5,7],[5,9]]))