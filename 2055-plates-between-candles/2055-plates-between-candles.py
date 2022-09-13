class Solution(object):
    def platesBetweenCandles(self, s, queries):
        candles = []
        for x in range(len(s)):
            if s[x] == "|":
                candles.append(x)
        print(candles)
        res = []
        for x,y in queries:
            leftIndex = bisect.bisect_left(candles,x)
            rightIndex = bisect.bisect_right(candles,y)
            
            if rightIndex - leftIndex <= 1:
                res.append(0)
            else:
                res.append(candles[rightIndex-1] - candles[leftIndex] + 1 - (rightIndex-leftIndex))
        return res
            
                