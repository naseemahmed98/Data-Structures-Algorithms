class Solution(object):
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        
        memoization = {}
        def topDown(x):
            if x == 0:
                return nums[0]
            if x == 1:
                return max(nums[0],nums[1])
            if x in memoization:
                return memoization[x]
            memoization[x] = max(nums[x]+topDown(x-2),topDown(x-1))
            return memoization[x]
        
        return topDown(len(nums)-1)
        