

    
class Solution(object):
    def climbStairs(self, n):
        def dp(step):
            if step == 0 or step == 1:
                return 1 
            if step in d:
                return d[step]
            d[step] = dp(step-1) + dp(step-2)
            return d[step]
        d = {}
        return dp(n)
    
    
    
