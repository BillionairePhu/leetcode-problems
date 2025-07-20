from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        results = [folder[0]]
        
        parent = folder[0] + "/"
        for element in folder:
            if (element + "/" == parent):
                continue
            if (element.startswith(parent)):
                continue
            results.append(element)
            parent = element + "/"
        return results
        
            