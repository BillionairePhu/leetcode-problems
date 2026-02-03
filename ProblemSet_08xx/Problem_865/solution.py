# Definition for a binary tree node.
from typing import Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxDepth = 0
        def dfs(node: TreeNode, currDepth: int):
            nonlocal maxDepth
            maxDepth = max(maxDepth, currDepth)
            if (node.left):
                dfs(node.left, currDepth+1)
            if (node.right):
                dfs(node.right, currDepth+1)
        dfs(root, 0)
        
        smallestSubtree = None
        def findSmallestSubtree(node: TreeNode, currDepth: int) -> bool:
            nonlocal maxDepth
            nonlocal smallestSubtree
            left, right = False, False
            if (node.left):
                left = findSmallestSubtree(node.left, currDepth+1)
            if (node.right):
                right = findSmallestSubtree(node.right, currDepth+1)
            if (currDepth == maxDepth):
                smallestSubtree = node
                return True
            if (left and right):
                smallestSubtree = node
            return left or right
        findSmallestSubtree(root, 0)
        return smallestSubtree
    
s = Solution()
node4 = TreeNode(4)
node7 = TreeNode(7)
node6 = TreeNode(6)
node0 = TreeNode(0)
node8 = TreeNode(8)
node2 = TreeNode(2, node7, node4)
node5 = TreeNode(5, node6, node2 )
node1 = TreeNode(1, node0, node8)
node3 = TreeNode(3, node5, node1)
print("Result", s.subtreeWithAllDeepest(node3).val)