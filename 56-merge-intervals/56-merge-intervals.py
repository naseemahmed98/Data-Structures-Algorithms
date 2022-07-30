class Solution(object):
    def merge(self, intervals):
        
        intervals.sort()
        res = [intervals[0]]
        
        for x in intervals:
            if res[-1][1] < x[0]:
                res.append(x)
            else:
                res[-1][1] = max(res[-1][1], x[1])
        return res