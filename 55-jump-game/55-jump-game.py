class Solution:
    def canJump(self, nums):
        
        flag = len(nums)-1
        for x in range(len(nums)-2,-1,-1):
            if nums[x] + x >= flag:
                flag = x 
        if flag == 0:
            return True
        return False