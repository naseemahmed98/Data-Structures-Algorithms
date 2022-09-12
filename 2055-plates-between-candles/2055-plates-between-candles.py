class Solution(object):
    def platesBetweenCandles(self, s, queries):
        
        candles = []
        for i in range(len(s)):
            if s[i] == '|':
               candles.append(i)
        res = []
        for l, r in queries:
            if l == r or not candles:
                res.append(0)
                continue
            i = bisect_left(candles, l)
            j = bisect_right(candles, r) - 1
            n = (candles[j]- candles[i] - 1) - (j - i - 1)
            res.append(max(n, 0))
        return res