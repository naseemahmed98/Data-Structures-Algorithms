class Solution:
    def minCostClimbingStairs(self, cost):
        memoization = {}
        
        def topDown(x):
            if x == 0 or x == 1:
                return cost[x]
            if x in memoization:
                return memoization[x]
            memoization[x] = min(topDown(x-1),topDown(x-2)) + cost[x]
            return memoization[x]
        
        return min(topDown(len(cost)-1),topDown(len(cost)-2))