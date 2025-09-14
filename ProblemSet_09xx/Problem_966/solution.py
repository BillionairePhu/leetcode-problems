from typing import List


class Solution:
  def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
    vowels = {"a", "e", "i", "o", "u"}
    result = []
    wordset = set(wordlist)
    lower_worddict:dict[str, list[int]] = {}
    processed_worddict:dict[str, list[int]] = {}
    
    for i, word in enumerate(wordlist):
      lower_word = word.lower()
      processed_word = "".join("_" if c in vowels else c for c in lower_word)
      if lower_word not in lower_worddict:
        lower_worddict[lower_word] = i
      if processed_word not in processed_worddict:
        processed_worddict[processed_word] = i
    
    for query in queries:
      if (query in wordset):
        result.append(query)
        continue
      
      lower_query = query.lower()
      if (lower_query in lower_worddict):
        word_index = lower_worddict[lower_query]
        result.append(wordlist[word_index])
        continue
      
      processed_query = "".join("_" if c in vowels else c for c in lower_query)
      if (processed_query in processed_worddict):
        word_index = processed_worddict[processed_query]
        result.append(wordlist[word_index])
        continue
      
      result.append("")
      
    return result
        
s = Solution()
print(s.spellchecker(["KiTe","kite","hare","Hare"], ["keti","keet","keto"]))