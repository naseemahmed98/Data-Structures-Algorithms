class Solution(object):
    def platesBetweenCandles(self, s, queries):
        p = [x for x in range(len(s)) if s[x] == "|"]
        res = []
        for x, y in queries:
            l = bisect.bisect_left(p,x)
            r = bisect.bisect_right(p,y)
            if r - l <= 1:
                res.append(0)
            else:
                res.append(p[r-1] - p[l] + 1 - (r-l))
        return res
        