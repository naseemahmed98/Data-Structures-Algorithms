class Solution:
    def minCostClimbingStairs(self, cost):
        cost = deque(cost)
        cost.appendleft(0)
        for x in range(2,len(cost)):
            print(cost[x-1],cost[x-2])
            cost[x] = min(cost[x-1]+cost[x], cost[x-2]+cost[x])
        return min(cost[-1],cost[-2])