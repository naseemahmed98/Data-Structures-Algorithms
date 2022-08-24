class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        preMap = collections.defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visitedSet = set()
        
        def dfs(crs):
            if crs in visitedSet:
                return False
            if len(preMap[crs]) == 0:
                return True
            visitedSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitedSet.remove(crs)
            preMap[crs] = []
            return True 
        
        for crs in range(numCourses):
            if dfs(crs) is False:
                return False
        return True
