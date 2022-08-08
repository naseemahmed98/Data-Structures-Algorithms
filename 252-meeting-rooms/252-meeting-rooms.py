class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x[0])
        for x in range(1,len(intervals)):
            if intervals[x][0] < intervals[x-1][1]:
                return False
        return True
    