class Solution(object):
    def rob(self, nums):
        dct = {}
        if len(nums) <= 3:
            return max(nums)
        def calculate_max_sum(nums,x,dct):
            #print(nums,x,dct)
            if x == 1:
                return max(nums[0],nums[1])
            if x == 0:
                return nums[0]
            if x in dct:
                return dct[x]
            max_sum = max(calculate_max_sum(nums,x-1,dct), calculate_max_sum(nums,x-2,dct) + nums[x])
            dct[x] = max_sum
            return max_sum
        
    
        shorter_length = len(nums)-1 
        
        #print(len(nums),nums[:len(nums)-1], nums[1:len(nums)])
        
        first_house = calculate_max_sum(nums[:shorter_length], shorter_length-1, {})
        second_house = calculate_max_sum(nums[1:], shorter_length-1,{})
        
        return max(first_house, second_house)