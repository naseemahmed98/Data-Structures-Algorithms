class Solution(object):
    def twoSum(self, nums, target):
        dct = {}
        for x in range(len(nums)):
            if target - nums[x] in dct:
                return x, dct[target-nums[x]]
            else:
                dct[nums[x]] = x