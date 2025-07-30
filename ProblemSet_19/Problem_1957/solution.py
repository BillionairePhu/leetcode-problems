class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        prev = s[0]
        count = 1
        for char in s[1:]:
            if (char == prev):
                count += 1
                
            else:
                prev = char
                count = 1
            
            if (count <= 2):
                    result += char
        return result