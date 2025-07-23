from typing import List

class Node:
    def __init__(self, start: int, end: int, mx: int, sm: int):
        self.left: Node | None = None
        self.right: Node | None = None
        self.start: int = start
        self.end: int = end
        self.mx: int = mx
        self.sm: int = sm
        
class SegmentTree:
    def __init__(self, n: int, m: int):
        self.n: int = n
        self.m: int = m
        
        def build(start: int, end: int) -> Node:
            if (start == end):
                return Node(start, end, m, m)
            
            mid = (start + end) // 2
            left_node = build(start, mid)
            right_node = build(mid+1, end)
            node = Node(start, end, m, left_node.sm + right_node.sm)
            node.left = left_node
            node.right = right_node
            return node
        self.root = build(0, n-1)
    
    def querySum(self, start: int, end: int) -> int:
        def queryHelper(node: Node, start: int, end: int) -> int:
            # print(start, end, node)
            if (start <= node.start and node.end <= end):
                return node.sm
            mid = (node.start + node.end) // 2
            if (end <= mid):
                return queryHelper(node.left, start, end)
            elif (start > mid):
                return queryHelper(node.right, start, end)
            return queryHelper(node.left, start, mid) + queryHelper(node.right, mid+1, end)
            
        return queryHelper(self.root, start, end)
    
    def queryMax(self, maxRow: int, k: int) -> int:
        def queryHelper(node: Node) -> list[int]:
            if (node.start == node.end):
                if (node.sm >= k and node.start <= maxRow):
                    return [node.start, self.m - node.sm]
                return []
            if (node.left.mx >= k):
                return queryHelper(node.left)
            return queryHelper(node.right)
        
        return queryHelper(self.root)
        
    def update(self, index: int, val: int):
        def updateHelper(node: Node):
            if (node.start == node.end):
                node.sm -= val
                node.mx -= val
                return
            mid = (node.start + node.end) // 2
            if (index <= mid):
                updateHelper(node.left)
            else:
                updateHelper(node.right)
            node.sm = node.left.sm + node.right.sm
            node.mx = max(node.left.mx, node.right.mx)
        updateHelper(self.root)
        
class BookMyShow:
    def __init__(self, n: int, m: int):
        self.segment_tree = SegmentTree(n, m)
        self.start_row = 0
        self.seats = [m] * n
        
    def gather(self, k: int, maxRow: int) -> list[int]:
        result = self.segment_tree.queryMax(maxRow, k)
        if (len(result) == 2):
            self.segment_tree.update(result[0], k)
            self.seats[result[0]] -= k
        return result
    
    def scatter(self, k: int, maxRow: int) -> bool:
        if (self.segment_tree.querySum(0, maxRow) < k):
            return False
        
        while k > 0:
            allocated_seats = min(self.seats[self.start_row], k)
            if (allocated_seats > 0):
                self.seats[self.start_row] -= allocated_seats
                self.segment_tree.update(self.start_row, allocated_seats)
                k -= allocated_seats
            if (self.seats[self.start_row] == 0):
                self.start_row += 1
        return True
        
myShow = BookMyShow(5, 5)

print(myShow.gather(4,0))
print(myShow.gather(2,0))
print(myShow.scatter(5,1))
print(myShow.scatter(5,1))

# myShow = BookMyShow(4, 5)

# print(myShow.scatter(6,2))
# print(myShow.gather(6,3))
# print(myShow.scatter(9,1))

# myShow = BookMyShow(5, 10)

# print(myShow.scatter(9,1))
# print(myShow.scatter(1,3))

# for i in range(5):
#     print(myShow.seats[i])
    
# print(myShow.gather(3,4))
# print(myShow.gather(1,1))
# print(myShow.gather(10,4))
