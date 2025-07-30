from typing import Counter, List


class TrieNode:
    def __init__(self, value: str = ''):
        self.value = value
        self.hash = None
        self.children: dict[str, TrieNode] = {}
        
class Solution:
    
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        counter = Counter()
        
        for path in paths:
            current_node = root
            for part in path:
                if (part not in current_node.children):
                    current_node.children[part] = TrieNode(part)
                current_node = current_node.children[part]
        self.construct(root, counter)
        print(counter)

        results = []
        path = []
        
        self.operate(root, counter, path, results)
        
        return results
        
    def construct(self, node: TrieNode, counter: Counter):
        if (len(node.children) == 0):
            node.hash = "()"
            return
        
        for child in node.children.values():
            self.construct(child, counter)
            
        sorted_keys = list(node.children.keys())
        sorted_keys.sort()
        children_hash = ""
        for key in sorted_keys:
            children_hash += f"{key}({node.children[key].hash})"
        node.hash = f"({children_hash})"
        counter[node.hash] += 1
        
    def operate(self, node: TrieNode, counter: Counter, path: list, results: list):
        if (counter[node.hash] > 1):
            return
        
        if (path):
            results.append(path[:])
        
        for folder, child in node.children.items():
            path.append(folder)
            self.operate(child, counter, path, results)
            path.pop()
        
        
        
s = Solution()
print(
    "Result",
    s.deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]])
)