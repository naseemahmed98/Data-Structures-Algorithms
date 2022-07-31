class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        counter = 0 #[0,1,2]
        for x in nums:
            if counter != x:
                return counter
            counter += 1
        return counter
        