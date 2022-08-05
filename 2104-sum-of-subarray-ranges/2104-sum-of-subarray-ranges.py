class Solution(object):
    def subArrayRanges(self, nums):
        l, r = 0, 1 
        max_val = nums[l]
        min_val = nums[l]
        total = 0 
        while l >= 0 and r < len(nums):
            max_val = max(max_val,nums[r])
            min_val = min(min_val,nums[r])
            total += max_val - min_val
            
            if r ==len(nums)-1:
                l += 1 
                r = l + 1 
                max_val, min_val = nums[l], nums[l]
            
            else:
                r += 1 
        return total
        