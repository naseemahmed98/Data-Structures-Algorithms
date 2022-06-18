class Solution(object):
    def maxSubArray(self, nums):
        
        total = max_ = nums[0]
        for i in nums[1:]: 
            total = max(i, total + i)
            max_ = max(total,max_)
        return max_