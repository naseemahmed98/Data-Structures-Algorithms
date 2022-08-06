class Solution(object):
    def subArrayRanges(self, nums):
        total = 0 
        l, r = 0, 1 
        max_val, min_val = nums[0], nums[0]
        while r < len(nums):
            max_val = max(max_val, nums[r])
            min_val = min(min_val, nums[r])
            total += max_val - min_val
            
            if r == len(nums)-1:
                max_val, min_val = nums[l+1], nums[l+1]
                l += 1 
                r = l + 1 
            
            else:
                r += 1 
        return total