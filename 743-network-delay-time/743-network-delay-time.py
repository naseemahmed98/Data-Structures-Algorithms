class Solution(object):
     def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for x,y,z in times:
            graph[x].append((y,z))
        
        distance = {}
        for x in range(1,N+1):
            distance[x] = float("inf")
        
        def dfs(node,totalTime):
            if distance[node] <= totalTime:
                return 
            distance[node] = totalTime
            
            graph[node].sort(key = lambda x: x[1])
            for nextNode, nextNodeTime in graph[node]:
                dfs(nextNode,totalTime+nextNodeTime)
            
            return
        
        
        dfs(K,0)
        res = max(list(distance.values()))
        return res if res < float("inf") else -1
    
    
