class Solution(object):
    def insert(self, intervals, newInterval):
        lst = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                lst.append(newInterval)
                return lst + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                lst.append(intervals[i])
            else:
                newInterval = (min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1]))
        
        lst.append(newInterval)
        return lst
        