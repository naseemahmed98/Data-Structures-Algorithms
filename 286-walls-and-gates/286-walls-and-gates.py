class Solution(object):
    def wallsAndGates(self, rooms):
        inf = 2147483647
        
        
        def bfs(q):
            while q:
                x,y,totalDistance = q.popleft()
                
                if x + 1 < rows and rooms[x+1][y] == inf:
                    q.append((x+1,y,totalDistance+1))
                    rooms[x+1][y] = totalDistance + 1
                if x- 1 >= 0 and rooms[x-1][y] == inf:
                    
                    q.append((x-1,y,totalDistance+1))
                    rooms[x-1][y] = totalDistance + 1
                if y+1 < cols and rooms[x][y+1] == inf:
                    
                    q.append((x,y+1,totalDistance+1))
                    rooms[x][y+1] = totalDistance + 1 
                if y-1 >= 0 and rooms[x][y-1] == inf:
                    
                    q.append((x,y-1,totalDistance+1))
                    rooms[x][y-1] = totalDistance +1
     
		
        rows, cols = len(rooms), len(rooms[0])
        q = deque()
        for x in range(rows):
            for y in range(cols):
                if rooms[x][y] == 0:
                    q.append((x,y,0))
        bfs(q)