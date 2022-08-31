class Solution(object):
    def coinChange(self, coins, amount):
        memoization = {}
        
        def topDown(num):
            if num == 0:
                return 0 
            if num in memoization:
                return memoization[num]
            memoization[num] = amount + 1
            for x in coins:
                if num >= x:
                    memoization[num] = min(memoization[num],1 + topDown(num-x))
            return memoization[num]
            
        return topDown(amount) if topDown(amount) < amount + 1 else -1
        
    
            
        
        
        
                
            