class Solution(object):
    def minimumOperations(self, nums):
        res = 0 
        deliveries = set()
        for x in nums:
            if x:
                deliveries.add(x)
        return len(deliveries)