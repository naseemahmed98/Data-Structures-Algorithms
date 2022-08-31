class Solution:
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
        
        
        visited = [-1]* (N+1)
        def bfs(queue):
            visited[queue[0]] = 0
            while queue:
                person = queue.popleft()
                for node in graph[person]:
                    if visited[person] == visited[node]:
                        return False
                    else:
                        if visited[node] == -1:
                            visited[node] = 1 - visited[person]
                            queue.append(node)
                    
            return True
        
        
        
        for x in range(1,N+1):
            if visited[x] == -1:
                if not bfs(deque([x])):
                    return False
        return True