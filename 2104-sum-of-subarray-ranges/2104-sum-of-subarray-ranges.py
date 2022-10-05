class Solution:
    def subArrayRanges(self, nums):
        
        total = 0
        left = 0
        right = 1
        mx = nums[left]
        mn = nums[left]
        
        while right < len(nums):            
            mx = max(mx, nums[right])
            mn = min(mn, nums[right])
            total +=  mx - mn
            
            if right == len(nums) - 1:
                left += 1
                right = left + 1
                mx = nums[left]
                mn = nums[left]
            else:
                right += 1
            
        return total