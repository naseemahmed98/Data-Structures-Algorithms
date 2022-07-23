class Solution(object):
    def twoSum(self, nums, target):
        dct = {}
        for x in range(len(nums)):
            if target-nums[x] not in dct:
                dct[nums[x]] = x
            else:
                return [dct[target-nums[x]],x]