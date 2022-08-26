class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap = collections.defaultdict(list)
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        res, visited = [], set()
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if not preMap[crs]:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            preMap[crs] = []
            visited.remove(crs)
            return True
        
        
        for x in range(numCourses):
            if not dfs(x):
                return False
        
        return True
        
        