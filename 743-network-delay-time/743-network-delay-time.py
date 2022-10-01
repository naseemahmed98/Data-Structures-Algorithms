class Solution(object):
     def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v)) # u --> v
        
        nodeTimes = {}
        
        
        def dfs(node, elasped):
            if node in nodeTimes and nodeTimes[node] <= elasped: 
                return
            nodeTimes[node] = elasped
            for time, nei in sorted(graph[node]):
                dfs(nei, time+elasped)
        dfs(K, 0)
        ans = max(nodeTimes.values())
        return ans if len(nodeTimes) == N else -1