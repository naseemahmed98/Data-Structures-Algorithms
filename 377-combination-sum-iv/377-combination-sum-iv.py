class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        for a in range(1,target + 1):
            for c in nums:
                if a >= c:
                    dp[a] = dp[a] + dp[a - c]
        return dp[target]