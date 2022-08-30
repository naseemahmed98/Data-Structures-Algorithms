class Solution(object):
     def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w)) 
        
        INF = float('inf')
        dist = {node: INF for node in range(1, N+1)}
        
        def dfs(node, elasped):
            if dist[node] <= elasped: 
                return
            dist[node] = elasped
            graph[node].sort(key = lambda x: x[1])
            for nextNode, time in graph[node]:
                dfs(nextNode, time+elasped)
        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < INF else -1