class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1 
        total,start = 0,0
        for x in range(len(gas)):
            total += gas[x]-cost[x]
            if total < 0:
                total = 0 
                start = x + 1
        return start
      