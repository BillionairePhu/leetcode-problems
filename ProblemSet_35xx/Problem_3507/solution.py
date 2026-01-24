from math import inf
from typing import List


class Node:
    def __init__(self, val: int, right = None):
        self.val: int = val
        self.right : Node|None = right

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        head = Node(nums[0])
        curr = head
        for i in range(1, len(nums)):
            newNode = Node(nums[i])
            curr.right = newNode
            curr = newNode
        
        def process(node: Node) -> tuple[bool, Node]:
            minSum = inf
            result = node
            isAscending = True
            while node.right != None:
                if (isAscending and node.val > node.right.val):
                    isAscending = False
                if (node.val + node.right.val < minSum):
                    minSum = node.val + node.right.val
                    result = node
                node = node.right
            return (isAscending, result)
        
        removal = 0
        while True:
            isAscending, mergeNode = process(head)
            if (isAscending):
                break
            
            newVal = mergeNode.val + mergeNode.right.val
            newRightNode = mergeNode.right.right
            
            mergeNode.val = newVal
            mergeNode.right = newRightNode
            removal += 1
            
        return removal
    
s = Solution()
print("Result", s.minimumPairRemoval([5,2,3,1]))
print("Result", s.minimumPairRemoval([1,2,2]))
