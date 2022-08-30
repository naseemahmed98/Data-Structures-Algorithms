class Solution(object):
    def networkDelayTime(self, times, n, k):
        
        networkMapping = collections.defaultdict(list)
        
        for x,y,z in times:
            networkMapping[x].append((y,z)) 

        signalTimes = {k:0}
        queue = deque([(k,0)])
        
        
        while queue:
            node,time = queue.popleft()
            for nextNode, nextNodeTime in networkMapping[node]:
                if nextNode == k: 
                    continue
                if (nextNode not in signalTimes) or (time + nextNodeTime < signalTimes[nextNode]):
                    signalTimes[nextNode] = time + nextNodeTime
                    queue.append((nextNode,signalTimes[nextNode]))
       
        return max(list(signalTimes.values())) if len(signalTimes) == n else -1