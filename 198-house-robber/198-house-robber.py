class Solution(object):
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        nums[1] = max(nums[0],nums[1])
        
        #dp = [2,7,0,0,0]
        
        for x in range(2,len(dp)):
            nums[x] = max(nums[x]+nums[x-2],nums[x-1])
        return nums[-1]
    