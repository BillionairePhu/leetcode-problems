from typing import List


class Solution:
    class TrieNode:
        def __init__(self):
            self.is_end_of_folder = False
            self.children: dict = {}
    
    def __init__(self):
        self.root = self.TrieNode()
    
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        results = []
        
        # Build Trie out of folders' paths
        for path in folder:
            parts = path.split('/')
            current_node = self.root
            for part in parts:
                if (part == ''):
                    continue
                if (part not in current_node.children):
                    current_node.children[part] = self.TrieNode()
                current_node = current_node.children[part]
            current_node.is_end_of_folder = True
            
        # Check if each path is a subfolder
        for path in folder:
            parts = path.split('/')
            is_subfolder = False
            
            current_node = self.root
            for i, part in enumerate(parts):
                if (part == ''):
                    continue
                
                if (i != len(parts) - 1):
                    current_node = current_node.children[part]
                    if (current_node.is_end_of_folder):
                        is_subfolder = True
                        break
            
            if (not is_subfolder):
                results.append(path)
        
        return results
                
s = Solution()
print("Result", s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))