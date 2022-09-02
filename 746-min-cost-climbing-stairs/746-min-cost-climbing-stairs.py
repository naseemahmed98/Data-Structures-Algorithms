class Solution:
    def minCostClimbingStairs(self, cost):
        for x in range(2,len(cost)):
            if x == len(cost)-1:
                cost[x] = cost[x] + cost[x-2]
            else:
                cost[x] = min(cost[x-1],cost[x-2])+ cost[x]
        return min(cost[-1],cost[-2])
        
        