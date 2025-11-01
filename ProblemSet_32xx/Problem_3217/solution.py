# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        forbidden_set = set(nums)
        curr, prev = head, None
        head = None
        while curr != None:
            if (curr.val in forbidden_set):
                if (prev == None):
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                if (head == None):
                    head = curr
                prev = curr
                curr = curr.next
        return head