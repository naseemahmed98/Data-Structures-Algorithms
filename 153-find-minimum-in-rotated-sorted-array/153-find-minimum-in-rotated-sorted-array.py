class Solution(object):
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while l < r:
            mid = (l + r) //2 
            if nums[mid] > nums[l]:
                l = mid 
            elif nums[mid] <= nums[l]:
                r = mid
        return nums[r+1]
 