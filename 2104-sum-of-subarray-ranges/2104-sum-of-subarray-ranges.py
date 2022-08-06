class Solution(object):
    def subArrayRanges(self, nums):
        summation = 0 
        max_num, min_num = nums[0], nums[0]
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                max_num = max(max_num,nums[y])
                min_num = min(min_num, nums[y])
                summation += max_num - min_num 
                
                if y == len(nums)-1:
                    max_num, min_num = nums[x+1], nums[x+1]
                
        return summation
    