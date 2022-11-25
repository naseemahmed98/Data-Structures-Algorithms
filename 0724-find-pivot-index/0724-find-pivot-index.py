class Solution(object):
    def pivotIndex(self, nums):
        leftArray = [0] * len(nums)
        rightArray = [0] * len(nums)
        summation = 0
        for x in range(len(nums)):
            leftArray[x] = summation 
            summation += nums[x]
        
        summation = 0 
        for x in range(len(nums)-1,-1,-1):
            rightArray[x] = summation 
            summation += nums[x]
        
        
        for x in range(len(nums)):
            if leftArray[x] == rightArray[x]:
                return x 
        
        return -1 
            
        
        