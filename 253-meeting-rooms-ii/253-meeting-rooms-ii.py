class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        start = []
        end = []
        for i in range(0, len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        start.sort()
        end.sort()
        count= 0
        rooms = 0
        while start and end:   
            #print(start, end, count, rooms)       
            if start[0] < end[0]:
                count+=1
                start.remove(start[0])
            else:
                end.remove(end[0])
                count-=1
                
            rooms = max(rooms, count)
        
        return rooms
            
        
        
        
        
        
      
        
        
      