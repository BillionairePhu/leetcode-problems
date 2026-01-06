
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = {}
        
        def traverse(node: TreeNode, level: int):
            if (level in level_sum):
                level_sum[level] += node.val
            else:
                level_sum[level] = node.val
            
            if (node.left != None):
                traverse(node.left, level+1)

            if (node.right != None):
                traverse(node.right, level+1)
        
        traverse(root, 1)

        result, result_value = 1, level_sum[1]
        for level, sum_value in level_sum.items():
            if sum_value > result_value:
                result_value = sum_value
                result = level
            elif (sum_value == result_value and level < result):
                result_value = sum_value
                result = level

        return result