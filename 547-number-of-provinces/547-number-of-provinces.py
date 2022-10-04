class Solution(object):
    def findCircleNum(self, isConnected):
        adjList = defaultdict(list)
        length = len(isConnected)
        for x in range(length):
            for y in range(length):
                if x != y and isConnected[x][y] == 1:
                    adjList[x].append(y)
        
        def bfs(x):
            q.append(x)
            while q:
               
                node = q.popleft()
                visited.add(node)
                for y in adjList[node]:
                    if y not in visited:
                        q.append(y)
                        
        
        
        visited = set()
        q = deque()
        numProvinces = 0 
        for x in range(length):
            if x not in visited:
                bfs(x)
                numProvinces += 1
        
        return numProvinces
        
        
        