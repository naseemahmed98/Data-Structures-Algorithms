class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0 
        l, r = 0, 1 
        while r < len(prices):
            diff = prices[r]-prices[l]
            if diff > max_profit:
                max_profit = diff 
            if prices[r] < prices[l]:
                l = r 
            r += 1 
        return max_profit
            
        