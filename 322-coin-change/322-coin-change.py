class Solution(object):
    def coinChange(self, coins, amount):
        dp = []
        for i in range(amount + 1):
            dp.append(sys.maxsize)
        dp[0] = 0 #basecase
        
        for c in coins: 
            for a in range(1,len(dp)):
                if a - c >= 0: 
                    dp[a] = min(dp[a],1+dp[a-c])
        
        return dp[amount] if dp[amount] != sys.maxsize else -1 