# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes: list[TreeNode] = []
        def traverse(node: TreeNode):
            nodes.append(node)
            if (node.left):
                traverse(node.left)
            if (node.right):
                traverse(node.right)
        traverse(root)
        nodes.sort(key=lambda x: x.val)
        
        print(len(nodes))
        root = nodes[(len(nodes) - 1) // 2]
        def build(node: TreeNode, left: int, right: int):
            if (right <= left):
                node.left = None
                node.right = None
                return
            
            middle = (left + right) // 2 
            left_child = (left + middle - 1) // 2
            if (left_child >= left and left_child < middle):
                node.left = nodes[left_child]
                build(nodes[left_child], left, middle-1)
            else:
                node.left = None
            right_child = (middle + 1 + right) // 2
            if (right_child > middle and right_child <= right):
                node.right = nodes[right_child]
                build(nodes[right_child], middle+1, right)
            else:
                node.right = None
        build(root, 0, len(nodes)-1)
        return root
    
node4 = TreeNode(4)
node3 = TreeNode(3, node4)
node2 = TreeNode(2, node3)
node1 = TreeNode(1, node2)
s = Solution()
s.balanceBST(node1)