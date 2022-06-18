class Solution(object):
    def lengthOfLIS(self, nums):
        lst = [1] * len(nums)
        for x in range(len(nums)-2, -1, -1):
            for y in range(x+1, len(nums)):
                if nums[x] < nums[y]:
                    lst[x] = max(lst[x], 1 + lst[y])
        return max(lst)
