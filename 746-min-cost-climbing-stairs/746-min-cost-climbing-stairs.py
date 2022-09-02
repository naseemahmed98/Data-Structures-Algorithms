class Solution:
    def minCostClimbingStairs(self, cost):
        dp = deque(cost)
        print(dp)
        dp.appendleft(0)
        
        for x in range(2,len(dp)):
            dp[x] = min(dp[x-1]+cost[x-1], dp[x-2]+cost[x-1])
        return min(dp[-2],dp[-1])