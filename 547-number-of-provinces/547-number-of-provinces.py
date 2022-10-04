class Solution(object):
    def findCircleNum(self, isConnected):
        adjList = defaultdict(list)
        length = len(isConnected)
        for x in range(length):
            for y in range(length):
                if x != y and isConnected[x][y] == 1:
                    adjList[x].append(y)
        
        def dfs(x):
            visited.add(x)
            for y in adjList[x]:
                if y not in visited:
                    dfs(y)
        
        
        visited = set()
        numProvinces = 0 
        for x in range(length):
            if x not in visited:
                dfs(x)
                numProvinces += 1
        
        return numProvinces
        
        
        