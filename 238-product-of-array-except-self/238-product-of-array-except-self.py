class Solution(object):
    def productExceptSelf(self, nums):
        lst = nums * 1 
        post = 1 
        for x in range(len(nums)-1,-1,-1):
            lst[x] = post
            post *= nums[x]
        pre = 1 
        for x in range(len(nums)):
            lst[x] *= pre 
            pre *= nums[x]
        return lst
            
