class Solution(object):
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        
        #dp = [2,7,0,0,0]
        
        for x in range(2,len(dp)):
            dp[x] = max(nums[x]+dp[x-2],dp[x-1])
        return dp[-1]
    