from typing import Counter, List


class Solution:
  def countMentions(self,
      numberOfUsers: int,
      events: List[List[str]]
      ) -> List[int]:
    events.sort(key=lambda x: (-int(x[1]), x[0]), reverse=True)
    
    next_online = [-1] * numberOfUsers
    mentions = [0] * numberOfUsers
    
    def process_mention(key: str, time: int, timestamp: int):
      if (key == "ALL"):
        for i in range(numberOfUsers):
          mentions[i] += time
      elif (key == "HERE"):
        for i in range(numberOfUsers):
          mentions[i] += time if next_online[i] <= timestamp else 0
      else:
        id = int(key[2:])
        mentions[id] += time
    
    for event_type, timestamp, content in events:
      if (event_type == "MESSAGE"):
        user_list = content.split()
        user_counter = Counter(user_list)
        for key, time in user_counter.items():
          process_mention(key, time, int(timestamp))
      else:
        next_online[int(content)] = int(timestamp) + 60
    
    return mentions
  
s = Solution()
# print("Result", s.countMentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]))
# print("Result", s.countMentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]))
# print("Result", s.countMentions(2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]))
print("Result", s.countMentions(3, [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]]))
        