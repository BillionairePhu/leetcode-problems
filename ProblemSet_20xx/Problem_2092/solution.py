from typing import List

class Person:
  def __init__(self, id: int):
    self.id = id
    self.hasAlreadySharedSecret = False
    self.related: list[Person] = []
    
  def shareSecret(self, secret_keepers: list[bool]):
    if (not secret_keepers[self.id]):
      return
    
    if (self.hasAlreadySharedSecret):
      return
    
    self.hasAlreadySharedSecret = True
    for related_person in self.related:
      if (not related_person.hasAlreadySharedSecret):
        secret_keepers[related_person.id] = True
        related_person.shareSecret(secret_keepers)

class Solution:
  def findAllPeople(self,
      n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    secret_keepers = [False for _ in range(n)]
    secret_keepers[0], secret_keepers[firstPerson] = True, True
    meetings.sort(key=lambda x: x[2])
    
    curr_time = 0
    curr_attendees: dict[int, Person] = {}
    for x, y, time in meetings:
      if (time > curr_time):
        for attendee in curr_attendees.values():
          attendee.shareSecret(secret_keepers)
        curr_attendees = {}
        curr_time = time
      
      if (x not in curr_attendees):
        curr_attendees[x] = Person(x)
      if (y not in curr_attendees):
        curr_attendees[y] = Person(y)
      curr_attendees[x].related.append(curr_attendees[y])
      curr_attendees[y].related.append(curr_attendees[x])
      
    for attendee in curr_attendees.values():
      attendee.shareSecret(secret_keepers)
    
    result = []
    for i in range(len(secret_keepers)):
      if (secret_keepers[i] == True):
        result.append(i)
    return result
        
        

s = Solution()
# print("Result", s.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))
# print("Result", s.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))
print("Result", s.findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1))