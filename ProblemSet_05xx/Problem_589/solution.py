"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from typing import List, Optional


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> List[int]:
        result = []
        def traverse(node: Node):
            result.append(node.val)
            if (not node.children):
                return
            for child in node.children:
                traverse(child)
        traverse(root)
        return result
    
s = Solution()
node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])
node2 = Node(2)
node4 = Node(4)
node1 = Node(1, [node3, node2, node4])
print("Result", s.preorder(node1))