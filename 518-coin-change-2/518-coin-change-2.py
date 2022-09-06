class Solution(object):
    def change(self, amount, coins):
        
        def f(i,target):
            if target == 0:
                return 1
            if i == len(coins):
                return 0
            if dp[i][target] != -1:
                return dp[i][target]
            take = 0
            if coins[i] <= target:
                take = f(i,target-coins[i])
            nottake = f(i+1,target)
            dp[i][target] = take + nottake
            return take + nottake
        dp = [[-1 for _ in range(amount+1)] for _ in range(len(coins))]
    
        a = f(0,amount)
        #print(dp)
        return a