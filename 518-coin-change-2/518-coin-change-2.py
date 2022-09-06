class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount+1)
        dp[0] = 1 
        
        for y in coins:
            if y <= amount:
                dp[y] += 1
            for x in range(y+1,amount+1):
                dp[x] += dp[x-y]
        
        return dp[-1]
        