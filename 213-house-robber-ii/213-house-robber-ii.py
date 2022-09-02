class Solution(object):
    def rob(self, nums):
    
        if len(nums) <=2:
            return max(nums)
        
        def houseRobber(array):
            dp = [0] * len(array)
            dp[0],dp[1] = array[0], max(array[0],array[1])
            for x in range(2,len(array)):
                dp[x] = max(array[x]+dp[x-2],dp[x-1])
            return dp[-1]
        
        
        
        return max(houseRobber(nums[:-1]),houseRobber(nums[1:]))
        