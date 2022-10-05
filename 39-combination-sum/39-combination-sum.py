class Solution(object):
    def combinationSum(self, candidates, target):
        dp = [[] for x in range(target+1)]
        
        for x in candidates:
            if x <= target:
                dp[x].append([x])
            for y in range(x+1,target+1):
                for z in dp[y-x]:
                    dp[y].append(z + [x])
        
        return dp[-1]
        