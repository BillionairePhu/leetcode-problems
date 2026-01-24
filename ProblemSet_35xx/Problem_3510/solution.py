from math import inf
from typing import List
from sortedcontainers import SortedList


class Node:
    def __init__(self, val: int, index: int, left = None, right = None):
        self.val: int = val
        self.index: int = index
        self.left: Node|None = left
        self.right: Node|None = right

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        head = Node(nums[0], 0)
        curr = head
        unordered = set()
        sumOrderedList: SortedList = SortedList()
        
        for i in range(1, len(nums)):
            newNode = Node(nums[i], i)
            
            sumOrderedList.add((curr.val + newNode.val, curr.index, curr))
            if (curr.val > newNode.val):
                unordered.add(curr)
            curr.right = newNode
            newNode.left = curr
            curr = newNode
        
        removal = 0
        while len(unordered) > 0:
            minSum, index, mergedNode = sumOrderedList[0]
            originalVal = mergedNode.val
            mergedNode.val = minSum
            removedNode = mergedNode.right
            mergedNode.right = removedNode.right
            if (mergedNode.right):
                mergedNode.right.left = mergedNode
            
            # Remove unordered item and sum related to the removed node
            if (removedNode in unordered):
                unordered.remove(removedNode)
            if (removedNode.right):
                sumOrderedList.remove(
                    (removedNode.val + removedNode.right.val, removedNode.index, removedNode))
                
            # Update unordered item and sum related to the merged node
            if (mergedNode in unordered):
                unordered.remove(mergedNode)
            if (mergedNode.right and mergedNode.val > mergedNode.right.val):
                unordered.add(mergedNode)
            sumOrderedList.remove((originalVal + removedNode.val, mergedNode.index, mergedNode))
            if (mergedNode.right):
                sumOrderedList.add((mergedNode.val + mergedNode.right.val, mergedNode.index, mergedNode))
                
            prevNode = mergedNode.left
            if (prevNode):
                if (prevNode in unordered):
                    unordered.remove(prevNode)
                if (prevNode.val > mergedNode.val):
                    unordered.add(prevNode)
                sumOrderedList.remove((originalVal + prevNode.val, prevNode.index, prevNode))
                sumOrderedList.add((mergedNode.val + prevNode.val, prevNode.index, prevNode))
            removal += 1
            
        return removal
    
s = Solution()
# print("Result", s.minimumPairRemoval([5,2,3,1]))
# print("Result", s.minimumPairRemoval([1,2,2]))
print("Result", s.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1]))