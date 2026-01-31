import heapq
from typing import List


class Node:
    def __init__(self, index):
        self.index = index
        self.edges: dict[int, int] = {}

    def __str__(self):
        return str(self.edges)


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        nodes: dict[int, Node] = {i: Node(i) for i in range(n)}

        for u, v, w in edges:
            if v in nodes[u].edges:
                nodes[u].edges[v] = min(nodes[u].edges[v], w)
            else:
                nodes[u].edges[v] = w

            if u in nodes[v].edges:
                nodes[v].edges[u] = min(nodes[v].edges[u], w * 2)
            else:
                nodes[v].edges[u] = w * 2

        # for node in nodes.values():
        #     print(node.index)
        #     print(node)

        djikstraTable = {0: 0}
        heap = []

        def addEdgesOfNodeToHeap(node: Node):
            currNodeWeight = djikstraTable[node.index]
            for destination, weight in node.edges.items():
                if destination not in djikstraTable:
                    # print("added", destination, currNodeWeight+weight)
                    heapq.heappush(heap, (currNodeWeight + weight, destination))

        addEdgesOfNodeToHeap(nodes[0])

        while len(heap) > 0:
            weight, index = heapq.heappop(heap)
            if index not in djikstraTable:
                print(index, weight)
                djikstraTable[index] = weight
                addEdgesOfNodeToHeap(nodes[index])
        # print(djikstraTable)

        return djikstraTable[n - 1] if (n - 1 in djikstraTable) else -1
