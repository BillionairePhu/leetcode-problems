

from collections import deque


class Solution:
  def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
    modulo = 10**9 + 7
    spread = 0
    queue = deque([0] * (forget-1) + [1])
    for _ in range(1, n):
      forget_people = queue.popleft()
      spread = spread - forget_people + queue[forget - delay - 1]
      queue.append(spread % modulo)
    return sum(list(queue)) % modulo
      
    
s = Solution()
print("Result", s.peopleAwareOfSecret(6, 2, 4))
print("Result", s.peopleAwareOfSecret(4, 1, 3))