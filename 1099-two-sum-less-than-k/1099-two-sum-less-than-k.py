class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0,len(nums)-1 
        largestPossibleSum = -1
        while l < r: 
            mySum = nums[r] + nums[l] 
            if mySum < k:
                largestPossibleSum = max(largestPossibleSum,mySum)
                l += 1 
            elif mySum >= k:
                r -= 1 
        return largestPossibleSum 


