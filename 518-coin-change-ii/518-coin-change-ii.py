class Solution(object):
    def change(self, amount, coins):
    
        
        def dp(coin,amount):
            if amount == 0:
                return 1 
            
            if coin == len(coins):
                return 0
            if memo[coin][amount] != -1:
                return memo[coin][amount]
            
            take = 0 
            if coins[coin] <= amount:
                take = dp(coin,amount-coins[coin])
            notTake = dp(coin+1,amount)
            memo[coin][amount] = take + notTake
            return take + notTake
    
        memo = [[-1 for x in range(amount+1)] for y in range(len(coins))]
        return dp(0,amount)