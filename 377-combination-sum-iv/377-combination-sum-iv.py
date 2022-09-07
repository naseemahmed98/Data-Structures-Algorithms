class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1 
        
        for x in range(1,target+1):
            for y in nums:
                if x >= y:
                    dp[x] += dp[x-y]
        return dp[-1]