class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        ans = 0
        d1 = {}
        for i in nums1:
            for j in nums2:
                if (i + j) in d1:
                    d1[i + j] += 1
                else:
                    d1[i +j] = 1
        for i in nums3:
            for j in nums4:
                target = -(i+j)
                if target in d1:
                    ans += d1[target]
            
        return ans
        