class Solution(object):
    def findCircleNum(self, isConnected):
        graph = collections.defaultdict(list)
        for x in range(len(isConnected)):
            for y in range(len(isConnected)):
                if isConnected[x][y] == 1:
                    graph[x].append(y)
        
        def dfs(node):
            visited.add(node)
            for city in graph[node]:
                if city not in visited:
                    dfs(city)
        
        visited = set()
        numProvinces = 0 
        for x in range(len(isConnected)):
            if x not in visited:
                numProvinces += 1 
                dfs(x)
        
        return numProvinces
        