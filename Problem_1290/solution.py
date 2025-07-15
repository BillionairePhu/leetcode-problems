# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        while head != None:
            result = result << 1
            result += head.val
            head = head.next
        return result
    
node1 = ListNode(1)
node2 = ListNode(0, node1)
node3 = ListNode(1, node2)

s = Solution()
print('Result', s.getDecimalValue(node3))