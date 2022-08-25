class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit, cycle = set(), set()
        res = []
        
        def dfs(pre):
            if pre in cycle:
                return False
            if pre in visit:
                return True
            cycle.add(pre)
            for crs in preMap[pre]:
                if not dfs(crs):
                    return False
            cycle.remove(pre)
            visit.add(pre)
            res.append(pre)
            return True 
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        

        
        
        
        
        
            
        