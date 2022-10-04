from collections import deque
class Solution(object): #BFS
    def numIslands(self, grid):
        
        def dfs(x,y):
            grid[x][y] = '0'
            if x+1 < rows and grid[x+1][y] == '1':
                dfs(x+1,y)
            if x-1 >= 0 and grid[x-1][y] == '1':
                dfs(x-1,y)
            if y+1 < cols and grid[x][y+1] == '1':
                dfs(x,y+1)
            if y-1 >= 0 and grid[x][y-1] == '1':
                dfs(x,y-1)
        
        
    
        numIslands = 0 
        rows, cols = len(grid), len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    dfs(x,y)
                    numIslands += 1 
        
        return numIslands
                    
                