class Solution(object):
    def subArrayRanges(self, nums):
        total = 0 
        max_val, min_val = nums[0], nums[0]
        
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                max_val, min_val = max(max_val,nums[y]), min(min_val,nums[y])
                total += max_val - min_val
                
                if y == len(nums)-1:
                    max_val, min_val = nums[x+1], nums[x+1]
        return total