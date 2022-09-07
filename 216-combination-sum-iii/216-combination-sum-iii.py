class Solution(object):
    def combinationSum3(self, k, n):
        dp = [[] for x in range(n+1)]
        characters = list(range(1,10))
        dp[0].append(())
        
        for x in characters:
            for y in range(n,x-1,-1):
                for z in dp[y-x]:
                    dp[y].append(z+(x,))
        res = []
        for x in (dp[-1]):
            if len(x) == k:
                res.append(x)
        return res