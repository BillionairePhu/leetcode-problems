class Solution:
  def findLexSmallestString(self, s: str, a: int, b: int) -> str:
    def mutate(num_list: list[int], a: int) -> list[int]:
      return [
        (num_list[i] if i%2 == 0 else (num_list[i]+a)%10)
          for i in range(len(num_list))
      ]
      
    def rotate(num_list: list[int], b: int) -> list[int]:
      return num_list[len(num_list)-b:] + num_list[0:len(num_list)-b]
    
    
    string_set = set()
    stack = [s]
    result = s
    while len(stack) > 0:
      if stack[-1] in string_set:
        stack.pop()
      else:
        result = min(result, stack[-1])
        
        array = list(map(int, stack[-1]))
        string_set.add(stack[-1])
        
        stack.pop()
        rotated = [str(num) for num in rotate(array, b)]
        mutated = [str(num) for num in mutate(array, a)]
        stack.append("".join(rotated))
        stack.append("".join(mutated))
    return result
  
s = Solution()
print("Result", s.findLexSmallestString("5525", 9, 2))
