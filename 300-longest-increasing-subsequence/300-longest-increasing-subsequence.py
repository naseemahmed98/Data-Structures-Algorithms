class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        
        for x in range(len(nums)-2,-1,-1):
            for y in range(x+1,len(nums)):
                if nums[x] < nums[y]:
                    dp[x] = max(dp[x],1+dp[y])
        
        return max(dp)