class Solution(object):
    def containsDuplicate(self, nums):
        dct = {}
        for x in nums:
            if x in dct:
                return True
            else:
                dct[x] = 1 
        return False