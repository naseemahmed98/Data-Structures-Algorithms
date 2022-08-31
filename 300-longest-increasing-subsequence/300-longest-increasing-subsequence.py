class Solution(object):
    def lengthOfLIS(self, nums):
        total_number = len(nums)
        dp = [1 for _ in range(total_number)]
        for i in range(1, total_number):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

            