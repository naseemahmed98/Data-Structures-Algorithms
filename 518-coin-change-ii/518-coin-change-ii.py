class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount+ 1)
        dp[0] = 1 
        
        for y in coins:
            for x in range(1,amount+1):
                if x - y >= 0:
                    dp[x] += dp[x-y]
        return dp[-1]