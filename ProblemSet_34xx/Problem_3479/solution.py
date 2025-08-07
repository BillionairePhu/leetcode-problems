# Write your solution here
from typing import List

class Node:
    def __init__(self, start: int, end: int, max_val: int):
        self.start: int = start
        self.end: int = end
        self.max_val: int = max_val
        self.left: Node|None = None
        self.right: Node|None = None

class SegmentTree:
    def __init__(self, values: list[int]):
        def build(start: int, end: int) -> Node:
            if (start == end):
                return Node(start, end, values[start])
            
            mid = (start + end) // 2
            left = build(start, mid)
            right = build(mid + 1, end)
            
            curr_node = Node(start, end, max(left.max_val, right.max_val))
            curr_node.left = left
            curr_node.right = right
            return curr_node
        self.root = build(0, len(values)-1)
    
    def query(self, value:int) -> int:
        def _query(node: Node, value: int) -> int:
            if (node.start == node.end):
                return node.start if node.max_val >= value else -1
            if (node.left.max_val >= value):
                return _query(node.left, value)
            return _query(node.right, value)
        
        return _query(self.root, value)
    
    def update(self, index:int, value: int) -> int:
        def _update(node: Node, index: int, value: int) -> int:
            if (node.start == node.end):
                node.max_val = value
                return
            mid = (node.start + node.end) // 2
            if (index <= mid):
                _update(node.left, index, value)
            else:
                _update(node.right, index, value)
            node.max_val = max(node.left.max_val, node.right.max_val)
        _update(self.root, index, value)
    

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        tree = SegmentTree(baskets)
        result = 0
        for fruit in fruits:
            basket_index = tree.query(fruit)
            if (basket_index == -1):
                result += 1
            else:
                tree.update(basket_index, 0)
        return result
    
s = Solution()
# print('Result', s.numOfUnplacedFruits([4,2,5], [3, 5, 4]))
print('Result', s.numOfUnplacedFruits([3,6,1], [6,4,7]))