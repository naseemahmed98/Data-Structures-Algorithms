class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0 
        for x in range(1,amount+1):
            for y in coins:
                if x >= y:
                    dp[x] = min(dp[x],1+dp[x-y])
        return dp[-1] if dp[-1] < amount+1 else -1
            