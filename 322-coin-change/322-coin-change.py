class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        
        def check(amount):
            if amount in memo: 
                return memo[amount]
            if amount == 0: 
                return 0
            if amount < 0: 
                return float("inf")
            memo[amount] = min([1 + check(amount - coin) for coin in coins])
            return memo[amount]
        
        minimum = check(amount)
        return minimum if minimum != float("inf") else -1