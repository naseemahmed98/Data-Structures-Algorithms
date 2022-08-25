class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit, cycle = set(), set()
        res = []
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True 
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        

        
        
        
        
        
            
        