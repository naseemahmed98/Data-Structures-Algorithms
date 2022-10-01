class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        for x,y,z in times:
            graph[x].append((y,z))
        
        
        nodeTimes = {k:0}
        
        q = collections.deque()
        q.append((k,0))
        
        while q:
            node, totalTime = q.pop()
            for nextNode, timeAddition in graph[node]:
                if nextNode not in nodeTimes or nodeTimes[nextNode] > totalTime + timeAddition:
                    nodeTimes[nextNode] = totalTime + timeAddition
                    q.append((nextNode,nodeTimes[nextNode]))
        
        return max(nodeTimes.values()) if len(nodeTimes) == n else -1