class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        maximum = 0 
        for x in nums:
            if (x - 1) not in nums_set:
                length = 1 
                while (x + length) in nums_set:
                    length += 1 
                maximum = max(length, maximum)
        return maximum 