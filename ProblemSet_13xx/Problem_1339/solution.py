# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        my_sum = 0
        
        def traverse(node: TreeNode):
            nonlocal my_sum
            my_sum += node.val
            
            if (node.left):
                traverse(node.left)
                
            if (node.right):
                traverse(node.right)
        
        traverse(root)
        
        result = 0
        def traverse_cut(node: TreeNode) -> int:
            nonlocal result
            left = 0
            if (node.left != None):
                left = traverse_cut(node.left)
                remaining = my_sum - left
                result = max(result, remaining * left)
            
            right = 0
            if (node.right != None):
                right = traverse_cut(node.right)
                remaining = my_sum - right
                result = max(result, remaining * right)
            
            return left + right + node.val
        
        traverse_cut(root)
        return result % (10**9 + 7)