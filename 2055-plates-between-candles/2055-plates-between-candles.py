class Solution(object):
    def platesBetweenCandles(self, s, queries):
        candles = []
        for x in range(len(s)):
            if s[x] == "|":
                candles.append(x)
        
        
        res = []
        for x,y in queries:
            l, r = bisect.bisect_left(candles,x),bisect.bisect_right(candles,y)
            
            if r - l <= 1:
                res.append(0)
            
            else:
                res.append((candles[r-1]-candles[l]+1) - (r-l))
        
        return res
            