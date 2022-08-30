class Solution(object):
     def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v)) # u --> v
        
        INF = float('inf')
        dist = {node: INF for node in range(1, N+1)}
        
        def dfs(node, elasped):
            if dist[node] <= elasped: return
            dist[node] = elasped
            for time, nei in sorted(graph[node]):
                dfs(nei, time+elasped)
        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < INF else -1