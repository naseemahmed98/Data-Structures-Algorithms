class Solution(object):
    def combinationSum4(self, nums, target):
        memoization = {}
        def dp(amount):
            if amount == 0:
                return 1
            if amount in memoization:
                return memoization[amount]
            memoization[amount] = 0 
            for x in nums:
                if amount >= x:
                    memoization[amount] = memoization[amount] + dp(amount-x)
            return memoization[amount]
        
        return dp(target)