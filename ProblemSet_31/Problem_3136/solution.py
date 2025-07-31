import string

class Solution:
    def isValid(self, word: str) -> bool:
        if (len(word) < 3):
            return False
        
        alphabet = string.ascii_letters + string.digits
        vowel = "aeiouAEIOU"
        hasVowel = False
        hasConsonant = False
        for char in word:
            if (char not in alphabet):
                return False
            if (not hasVowel and char in vowel):
                hasVowel = True
            if (not hasConsonant and char in string.ascii_letters and char not in vowel):
                hasConsonant = True
        return hasConsonant and hasVowel            
        
s = Solution()
print("Result", s.isValid('UuE6'))