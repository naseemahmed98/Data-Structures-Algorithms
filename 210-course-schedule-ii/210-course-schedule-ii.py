class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        
        cycle, visited = set(), set()
        res = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visited:
                return True 
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for x in range(numCourses):
            if not dfs(x):
                return []
        
        return res
        
        
        
        
            
        