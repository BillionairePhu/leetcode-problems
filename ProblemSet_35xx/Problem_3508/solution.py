import bisect
from collections import deque
from typing import List


class Router:

  def __init__(self, memoryLimit: int):
    self.memoryLimit = memoryLimit
    self.queue = deque(maxlen=memoryLimit)
    self.destination_queues: dict[int, list[list[int]]] = {}
    self.packets_set = set()

  def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
    if (source, destination, timestamp) in self.packets_set:
      return False
    self.packets_set.add((source, destination, timestamp))

    if len(self.queue) >= self.memoryLimit:
      old_source, old_destination, old_timestamp = self.queue.popleft()
      # remove from per-destination list as well
      lst = self.destination_queues[old_destination]
      idx = bisect.bisect_left(lst, old_timestamp, key=lambda x: x[2])
      if idx < len(lst) and lst[idx][2] == old_timestamp:
        ele = lst.pop(idx)
        self.packets_set.remove((ele[0],ele[1],ele[2]))
      if not lst:
        del self.destination_queues[old_destination]

    new_packet = [source, destination, timestamp]
    self.queue.append(new_packet)

    if destination not in self.destination_queues:
      self.destination_queues[destination] = [new_packet]
    else:
      bisect.insort(
        self.destination_queues[destination],
        new_packet, key=lambda x: x[2]
      )

    return True

  def forwardPacket(self) -> List[int]:
    if not self.queue:
      return []
    src, dest, ts = self.queue.popleft()
    lst = self.destination_queues[dest]
    idx = bisect.bisect_left(lst, ts, key=lambda x: x[2])
    if idx < len(lst) and lst[idx][2] == ts:
      lst.pop(idx)
    if not lst:
      del self.destination_queues[dest]
    self.packets_set.remove((src, dest, ts))
    return [src, dest, ts]

  def getCount(self, destination: int, startTime: int, endTime: int) -> int:
    if destination not in self.destination_queues:
      return 0
    lst = self.destination_queues[destination]
    left = bisect.bisect_left(lst, startTime, key=lambda x: x[2])
    right = bisect.bisect_right(lst, endTime, key=lambda x: x[2])
    return right - left


# Your Router object will be instantiated and called as such:
obj = Router(3)
param1 = obj.addPacket(1, 4, 90)
print(param1)
param1 = obj.addPacket(2, 5, 90)
print(param1)
param1 = obj.addPacket(3, 5, 90)
print(param1)
param1 = obj.addPacket(4, 5, 90)
print(param1)
param1 = obj.addPacket(1, 4, 90)
print(param1)
# param2 = obj.forwardPacket()
# print(param2)
# param3 = obj.addPacket(3,4,5)
# print(param3)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
