from typing import List
from heapq import heappop, heappush

class TaskManager:

  def __init__(self, tasks: List[List[int]]):
    self.tasks_info = {}
    self.task_heap = []
    for task in tasks:
      userId, taskId, priority = task
      self.tasks_info[taskId] = [-priority, userId]
      heappush(self.task_heap, (-priority, -taskId))

  def add(self, userId: int, taskId: int, priority: int) -> None:
    self.tasks_info[taskId] = [-priority, userId]
    heappush(self.task_heap, (-priority, -taskId))

  def edit(self, taskId: int, newPriority: int) -> None:
    self.tasks_info[taskId][0] = -newPriority
    heappush(self.task_heap, (-newPriority, -taskId))

  def rmv(self, taskId: int) -> None:
    self.tasks_info.pop(taskId)

  def execTop(self) -> int:
    while len(self.task_heap) > 0:
      priority, taskId = heappop(self.task_heap)
      if (-taskId in self.tasks_info
          and self.tasks_info[-taskId][0] == priority):
        userId = self.tasks_info[-taskId][1]
        self.tasks_info.pop(-taskId)
        return userId
    return -1


# Your TaskManager object will be instantiated and called as such:
obj = TaskManager([[3,12,11],[6,2,46],[2,1,46],[5,23,21]])
print(obj.execTop())
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()