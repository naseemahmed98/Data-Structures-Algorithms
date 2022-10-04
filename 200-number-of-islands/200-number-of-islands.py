from collections import deque
class Solution(object): #BFS
    def numIslands(self, grid):
        
        visited = set()
        q = deque()
        
        def bfs(x,y):
            q.append((x,y))
            while q:
                x,y = q.popleft()
                
                if x+1 < rows and grid[x+1][y] == '1' and (x+1,y) not in visited:
                    q.append((x+1,y))
                    visited.add((x+1,y))
                if x-1 >= 0  and grid[x-1][y] == '1' and (x-1,y) not in visited:
                    q.append((x-1,y))
                    visited.add((x-1,y))
                if  y + 1 < cols and grid[x][y+1] == '1' and (x,y+1) not in visited:
                    q.append((x,y+1))
                    visited.add((x,y+1))
                if y-1 >= 0 and grid[x][y-1] == '1' and (x,y-1) not in visited:
                    q.append((x,y-1))
                    visited.add((x,y-1))
                
                    
            
            
        
    
        numIslands = 0 
        rows, cols = len(grid), len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1' and (x,y) not in visited:
                    bfs(x,y)
                    numIslands += 1 
        
        return numIslands
                    
                