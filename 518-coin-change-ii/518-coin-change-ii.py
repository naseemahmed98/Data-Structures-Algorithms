class Solution(object):
    def change(self, amount, coins):
        dp = [0] * (amount+1)
        dp[0] = 1 
        
        for x in coins:
            if x <= amount:
                dp[x] += 1 
            for y in range(x+1,amount+1):
                dp[y] += dp[y-x]
        
        return dp[-1]
      