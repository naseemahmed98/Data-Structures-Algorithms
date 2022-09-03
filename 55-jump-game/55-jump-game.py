class Solution:
    def canJump(self, nums):
        flag = 0
        if len(nums) == 1:
            return True
        
        for x in range(len(nums)):
            if x <= flag:
                if nums[x] + x >= flag:
                    flag = nums[x]+x
           
            if flag >= len(nums)-1:
                return True
            if x > flag:
                return False