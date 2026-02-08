# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(node: TreeNode, level: int = 0) -> tuple[bool, int]:
            """Return whether the tree under this node is balanced and the depth of that tree"""
            if (node.left == None and node.right == None):
                return True, level
            
            levels = []
            if (node.left):
                left_balanced, left_depth = traverse(node.left, level + 1)
                if (not left_balanced):
                    return False, level
                levels.append(left_depth)
            else:
                levels.append(level)
            if (node.right):
                right_balanced, right_depth = traverse(node.right, level + 1)
                if (not right_balanced):
                    return False, level
                levels.append(right_depth)
            else:
                levels.append(level)
            return max(levels) - min(levels) <= 1, max(levels)
        
        return traverse(root)[0] if root != None else True

s = Solution()
node4_1 = TreeNode(4)
node4_2 = TreeNode(4)
node3_1 = TreeNode(3, node4_1, node4_2)
node3_2 = TreeNode(3)
node2_1 = TreeNode(2)
node2_2 = TreeNode(2, node3_1, node3_2)
node1 = TreeNode(1, node2_1, node2_2)
print("Result", s.isBalanced(node1))