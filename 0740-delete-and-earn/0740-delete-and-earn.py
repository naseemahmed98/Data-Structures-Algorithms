class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = collections.defaultdict(int)
        for x in nums:
            freq[x] += 1 
        
        nums = list(set(nums))
        nums.sort()
        earn1, earn2 = 0,0 
        
    
            
        for x in range(len(nums)): 
            currEarnings = freq[nums[x]] * nums[x] 
            if x > 0 and nums[x] == 1 + nums[x-1]:
                temp = earn2 
                earn2 = max(earn2, earn1 + currEarnings)
                earn1 = temp 
                
            else:
                temp = earn2 
                earn2 += currEarnings 
                earn1 = temp
        
        return earn2
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        