class Solution:
    def compressedString(self, word: str) -> str:
        i, current_char, current_count = 0, None, 0
        result = []
        while i < len(word):
            if (word[i] == current_char):
                current_count += 1
            elif (current_char != None):
                result.append(str(current_count) + current_char)
                current_char = word[i]
                current_count = 1
            else:
                current_char = word[i]
                current_count = 1
            
            if current_count == 9:
                result.append(str(current_count) + current_char)
                current_char = None
                current_count = 0
            i += 1
        if (current_char != None):
            result.append(str(current_count) + current_char)
        return "".join(result)
    
s = Solution()
print("Result", s.compressedString("abcde"))