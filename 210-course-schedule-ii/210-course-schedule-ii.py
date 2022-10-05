class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        
        graph = defaultdict(list)
        
        for x,y in prerequisites:
            graph[x].append(y)
        
        memo, visited = {},set()
        
        def dfs(crs):
            if crs in memo:
                return memo[crs]
            if crs in visited:
                return False 
            
            visited.add(crs)
            for x in graph[crs]:
                if not dfs(x):
                    return False
            #visited.remove(crs)
            res.append(crs)
            memo[crs] = True
            return True
        
        

        res = []
        for x in range(numCourses):
            if not dfs(x):
                return []
        
        return res
        
        
        
        
        
            
        