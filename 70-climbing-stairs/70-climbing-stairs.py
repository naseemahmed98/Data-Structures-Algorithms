class Solution(object):
    def climbStairs(self, n):
        
        dp = [0] * (n+1)
        dp[0],dp[1] = 1, 1
        
  
        
        
        for x in range(2,n+1):
            dp[x] = dp[x-1] + dp[x-2]
        
        return dp[-1]
    
    
    

    
    
