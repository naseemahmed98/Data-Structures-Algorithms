class Solution(object):
    def findCircleNum(self, isConnected):
        visited = set()
        graph = collections.defaultdict(list)
        for x in range(len(isConnected)):
            for y in range(len(isConnected)):
                if isConnected[x][y] == 1:
                    graph[x].append(y)
        
        
        def bfs(node):
            visited.add(node)
            queue = deque()
            queue.append(node)
            while queue:
                currCity = queue.popleft()
                for x in graph[currCity]:
                    if x not in visited:
                        visited.add(x)
                        queue.append(x)
        
        numProvinces = 0 
        for x in range(len(isConnected)):
            if x not in visited:
                numProvinces += 1 
                bfs(x)
        return numProvinces
                
            
        