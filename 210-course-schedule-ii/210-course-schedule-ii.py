class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        cycle = set()
        res = []
        memo = {}
        def dfs(pre):
            if pre in cycle:
                return False
            if pre in memo:
                return memo[pre]
            cycle.add(pre)
            for crs in preMap[pre]:
                if not dfs(crs):
                    return False
            cycle.remove(pre)
            memo[pre] = True
            res.append(pre)
            return True 
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        

        
        
        
        
        
            
        