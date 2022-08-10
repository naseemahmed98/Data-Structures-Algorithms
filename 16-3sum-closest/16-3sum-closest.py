class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float("inf")
        for x in range(len(nums)):
            
            l, r = x+1, len(nums)-1
            while l < r:
                summation = nums[x] + nums[l] + nums[r] #sum of three numbers
                summation_diff = abs(target-summation)
                if summation_diff < closest_sum:
                    closest_sum = summation_diff
                    res = summation
                
                if summation > target:
                    r -= 1 
                elif summation < target:
                    l += 1
                else:
                    return summation
                
        return res
          
                    
                    
        