class Solution:
  def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    result = 0
    words = text.split()
    broken_set = set(brokenLetters)
    for word in words:
      valid = True
      for char in word:
        if (char in broken_set):
          valid = False
          break
      if (valid == True):
        result += 1
    return result