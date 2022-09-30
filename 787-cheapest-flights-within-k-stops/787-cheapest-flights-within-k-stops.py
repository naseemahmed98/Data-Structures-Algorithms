class Solution:
    def findCheapestPrice(self, n, flights, src, dest, k):
        dp = collections.defaultdict(list)
        for x,y,z in flights:
            dp[x].append((y,z))
        
        cityCost = {src:0}
        
        queue = collections.deque()
        
        queue.append((src,0,0))
        
        while queue:
            city, cost, distance = queue.popleft()
            for nextTrip,nextTripCost in dp[city]:
                if nextTrip not in cityCost or cost + nextTripCost < cityCost[nextTrip]:
                    cityCost[nextTrip] = cost + nextTripCost
                    if distance < k:
                        queue.append((nextTrip,cityCost[nextTrip],distance+1))
        
        return cityCost[dest] if dest in cityCost else -1 
    
        
        
    
        