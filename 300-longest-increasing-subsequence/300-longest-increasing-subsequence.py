class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        
        for x in range(1,len(nums)):
            for y in range(x):
                if nums[y] < nums[x]:
                    dp[x] = max(dp[x],1+dp[y])
        
        return max(dp)