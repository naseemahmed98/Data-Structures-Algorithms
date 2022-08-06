class Solution(object):
    def subArrayRanges(self, nums):
        total = 0 
        l, r = 0, 1
        max_num, min_num = nums[0], nums[0]
        while r < len(nums):
            max_num = max(max_num,nums[r])
            min_num = min(min_num, nums[r])
            total += max_num - min_num 
            
            if r == len(nums)-1:
                l += 1 
                r = l + 1 
                max_num, min_num = nums[l], nums[l]
                
            else:
                r += 1
        return total 