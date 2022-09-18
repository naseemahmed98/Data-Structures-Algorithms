class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                #checking j duplicates
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                l, r = j + 1, len(nums) - 1

                while l < r:
                    threeSum = nums[l] + nums[r] + nums[i] + nums[j]
                    if threeSum > target:
                        r -= 1
                    elif threeSum < target:
                        l += 1
                    else:
                        res.append([nums[l], nums[r], nums[i], nums[j]])
                        r -= 1
                        #checking l duplicates
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

        return res