class Solution(object):
    def maxProduct(self, nums):
        maximum = minimum = result = nums[0]
    
        for num in nums[1:]:
            temp = minimum
            minimum = min(num, num * maximum, num * minimum)
            maximum = max(num, num * maximum, num * temp)
            result = max(result, maximum)
        
        return result 