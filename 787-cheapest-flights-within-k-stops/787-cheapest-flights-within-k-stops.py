class Solution:
    def findCheapestPrice(self, n, flights, src, dest, k):
        dp = collections.defaultdict(list)
        for start, end, cost in flights:
            dp[start].append((end,cost))
        
        costMap = {src:0} 
        
        queue = deque([(src,0,0)])
        
        while queue:
            currFlight, cost, distance = queue.popleft()
            for nextTrip, nextTripCost in dp[currFlight]:
                if nextTrip not in costMap or costMap[nextTrip] > nextTripCost + cost:
                    costMap[nextTrip] = nextTripCost + cost
                    if distance < k:
                        queue.append((nextTrip,costMap[nextTrip],distance+1))
        
        return costMap[dest] if dest in costMap else -1
                    
        