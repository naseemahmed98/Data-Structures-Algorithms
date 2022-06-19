class Solution(object):
    def merge(self, intervals):
        if intervals == []:
            return []
        
        result = []
        intervals.sort()
        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result