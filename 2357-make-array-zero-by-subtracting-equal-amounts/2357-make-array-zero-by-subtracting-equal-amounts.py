class Solution(object):
    def minimumOperations(self, nums):
        res = set()
        for x in nums:
            if x != 0:
                res.add(x)
        return len(res)
            