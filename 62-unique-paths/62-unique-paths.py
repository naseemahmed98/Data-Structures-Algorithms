class Solution(object):
    def uniquePaths(self, m, n):
        
        
        memoization = {}
        def topDown(x,y):
            if x == 0 or y == 0:
                return 1 
            if (x,y) in memoization:
                return memoization[(x,y)]
            memoization[(x,y)] = topDown(x-1,y) + topDown(x,y-1)
            return memoization[(x,y)]
        
        return topDown(m-1,n-1)
            