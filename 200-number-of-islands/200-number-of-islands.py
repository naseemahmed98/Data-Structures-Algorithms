class Solution(object): #DFS
    def numIslands(self, grid):
        res = 0 
        rows = len(grid)
        cols = len(grid[0])

        def find_island(x,y):
            grid[x][y] = '0'
            
            if x + 1 < rows and grid[x+1][y] == '1': 
                find_island(x+1,y)
            
            if x - 1 >= 0 and grid[x-1][y] == '1':
                find_island(x-1,y)
            
            if y + 1 < cols and grid[x][y+1] == '1': 
                find_island(x,y+1)
            
            if y - 1 >= 0 and grid[x][y-1] == '1':
                find_island(x,y-1)
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    res+=1
                    find_island(x,y)
                    #res += 1 
        return res
