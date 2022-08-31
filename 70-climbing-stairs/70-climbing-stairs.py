

    
class Solution(object):
    def climbStairs(self, n):
        def topDown(step):
            if step == 0 or step == 1:
                return 1
            if step in dp:
                return dp[step]

            dp[step] = topDown(step-1) + topDown(step-2)
            
            return dp[step]
        dp = {}
        return topDown(n)
    
    
    

    
    
