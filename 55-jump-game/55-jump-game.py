class Solution:
    def canJump(self, nums):
    
        flag = len(nums) - 1
        
        for x in range(len(nums)-2,-1,-1):
            if x + nums[x] >= flag:
                flag = x 
        
        return True if flag == 0 else False