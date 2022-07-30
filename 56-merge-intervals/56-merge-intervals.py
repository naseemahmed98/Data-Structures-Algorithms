class Solution(object):
    def merge(self, intervals):
        if intervals == []:
            return [] 
        intervals.sort()
        result = []
        for x in intervals:
            if result == [] or result[-1][1] < x[0]:
                result.append(x)
            else:
                result[-1][1] = max(x[1], result[-1][1])
        return result 