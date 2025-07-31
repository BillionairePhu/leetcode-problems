from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folders_set = set(folder)
        results = []
        
        for element in folder:
            parts = element.split('/')
            isSubfolder = False
            path = '/'
            for i in range(1, len(parts)-1):
                path += parts[i]
                if (path in folders_set):
                    isSubfolder = True
                    break
                path += "/"
            if (not isSubfolder):
                results.append(element)
        return results
                
            
s = Solution()
print("Result", s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))