class Solution(object):
    def combinationSum3(self, k, n):
        dp = [set() for x in range(n+1)]
        characters = [i for i in range(1,10)]
        dp[0].add(())
        
        for x in characters:
            for y in range(n,x-1,-1):
                for z in dp[y-x]:
                    combo = z + (x,)
                    dp[y].add(combo)
        
        res = []
        for x in dp[-1]:
            if len(x) == k:
                res.append(x)
        
        return res
                    
                        