class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        for (x,y) , val in zip(equations,values):
            graph[x][y] = val
            graph[y][x] = 1 / val
        
        
        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1 
            
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i,y,visited)
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[x][i]
            
            return -1 
        
        
        res = []
        for x in queries:
            res.append(dfs(x[0],x[1],set()))
        
        return res 
            
            
        
        
        