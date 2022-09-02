class Solution:
    def minCostClimbingStairs(self, cost):
        dp = len(cost) * [0]
        dp[0], dp[1] = cost[0], cost[1]
        for x in range(2,len(cost)):
            dp[x] = min(dp[x-1],dp[x-2]) + cost[x]
        return min(dp[-1],dp[-2])
        
        