from collections import deque
class Solution(object): #BFS
    def numIslands(self, grid):
        
        q = deque()
        
        def bfs(x,y):
            q.append((x,y))
            while q:
                x,y = q.popleft()
                if x+1 < rows and grid[x+1][y] == '1':
                    q.append((x+1,y))
                    grid[x+1][y] = '0'
                if x-1 >= 0  and grid[x-1][y] == '1':
                    q.append((x-1,y))
                    grid[x-1][y] = '0'
                if  y + 1 < cols and grid[x][y+1] == '1':
                    q.append((x,y+1))
                    grid[x][y+1] = '0'
                if y-1 >= 0 and grid[x][y-1] == '1':
                    q.append((x,y-1))
                    grid[x][y-1] = '0'
                
                    
            
            
        
    
        numIslands = 0 
        rows, cols = len(grid), len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    bfs(x,y)
                    numIslands += 1 
        
        return numIslands
                    
                