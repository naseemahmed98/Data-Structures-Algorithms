class Solution:
    def combinationSum4(self, nums,target):
        memo = {}
        def dfs(t):
            if t == 0:
                return 1
            if t in memo:
                return memo[t]
            res = 0
            if t >= 0:
                for i in nums:
                    res += dfs(t-i)
                    memo[t] = res
            return res
        return (dfs(target))
    
    
