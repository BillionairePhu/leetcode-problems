from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def delete(left_index: int, right_index:int) -> int:
            if (left_index >= len(s1) and right_index >= len(s2)):
                return 0
            
            if (left_index >= len(s1)):
                return delete(left_index, right_index+1) + ord(s2[right_index])
            
            if (right_index >= len(s2)):
                return delete(left_index+1, right_index) + ord(s1[left_index])
            
            # If the current character at two strings are equal, do not delete
            if (s1[left_index] == s2[right_index]):
                return delete(left_index+1, right_index+1)
            
            # Case 1: delete the character on the left
            left = delete(left_index + 1, right_index) + ord(s1[left_index])
            
            # Case 2: delete the character on the right
            right = delete(left_index , right_index + 1) + ord(s2[right_index])
            
            return min(left, right)
        
        return delete(0, 0)
    
s = Solution()
print("Result", s.minimumDeleteSum("sea", "eat"))
print("Result", s.minimumDeleteSum("delete", "leet"))


            