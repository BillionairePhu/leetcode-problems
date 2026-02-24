from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        def traverse(node: Optional[TreeNode], parent_value: int):
            nonlocal result
            if (node is None):
                return
            if (node.left is None and node.right is None):
                result += (parent_value << 1) + node.val
            else:
                traverse(node.left, (parent_value << 1) + node.val)
                traverse(node.right, (parent_value << 1) + node.val)
        traverse(root, 0)
        return result
    
s = Solution()
node_grandchild1 = TreeNode(0)
node_grandchild2 = TreeNode(1)
node_grandchild3 = TreeNode(0)
node_grandchild4 = TreeNode(1)
node_child1 = TreeNode(0, node_grandchild1, node_grandchild2)
node_child2 = TreeNode(1, node_grandchild3, node_grandchild4)
node_parent = TreeNode(1, node_child1, node_child2)
print("Result", s.sumRootToLeaf(node_parent))