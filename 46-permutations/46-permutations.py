class Solution(object):
    def permute(self, nums):
        def helper(ind):
            if ind==len(nums):
                res.append(nums[:])
                return
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                helper(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]
        
        res=[]
        helper(0)
        return res
        