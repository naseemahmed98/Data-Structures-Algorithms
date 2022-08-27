class Solution:
    def findCheapestPrice(self, n, flights, src, dest, k):
        dp = defaultdict(list)
        for i,j,w in flights: 
            dp[i].append((j,w)) 

        q = deque([(src,0,0)])
        visited = set()
        res = float("inf")
        costMap = {src:0}

        while q: 
            node,dist,cost = q.popleft()
            for i,w in dp[node]: 
                if i not in costMap or cost+w<costMap[i] : 
                    costMap[i] = w+cost
                    if dist<k:
                        q.append((i,dist+1,cost+w))  

        return costMap[dest] if dest in costMap else -1