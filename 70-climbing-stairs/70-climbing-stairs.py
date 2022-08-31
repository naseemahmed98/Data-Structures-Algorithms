class Solution(object):
    def climbStairs(self, n):
        def dp(n):
            if n == 0 or n == 1:
                return 1 
            if n in d:
                return d[n]
            d[n] = dp(n-1) + dp(n-2)
            return d[n]
        d = {}
        return dp(n)