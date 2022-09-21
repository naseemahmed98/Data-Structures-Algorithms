class Solution(object):
    def twoSumLessThanK(self, nums, k):
        nums.sort() #60,75,85,90,120,125,150
        l, r = 0,len(nums)-1 
        largestPossibleSum = float("-inf")
        while l < r: 
            mySum = nums[r] + nums[l]
            if mySum >= k:
                r -= 1 
            if mySum < k:
                if mySum > largestPossibleSum:
                    largestPossibleSum = mySum
                l += 1 
        return largestPossibleSum if largestPossibleSum > float("-inf") else -1 
        