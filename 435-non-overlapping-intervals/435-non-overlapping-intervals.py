class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        res = 0 
        intervals.sort()
        prevEnd = float("-inf")
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
                