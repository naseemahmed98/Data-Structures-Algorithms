class Solution:
    def possibleBipartition(self, N, dislikes):
        graph = collections.defaultdict(list)
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
            
            
        def dfs(node, col):
            color[node] = col
            for neigh in graph[node]:
                if color[neigh] == color[node]:
                    return False
                if color[neigh] == 0 and not dfs(neigh, -col):
                    return False
            return True 
        
        
        color = [0] * (N+1)  
        for i in range(1,N):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True