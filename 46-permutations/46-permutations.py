class Solution(object):
    def permute(self, nums):
        def helper(ind):
            if ind == len(nums):
                res.append(nums[:])
                return 
            for x in range(ind,len(nums)):
                nums[ind],nums[x] = nums[x],nums[ind]
                helper(ind+1)
                nums[ind],nums[x] = nums[x],nums[ind]
        
        res = []
        helper(0)
        
        return res