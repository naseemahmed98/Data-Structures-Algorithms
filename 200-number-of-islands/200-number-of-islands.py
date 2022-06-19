class Solution:
    def numIslands(self, grid):
        visited = set()
        row,col=len(grid),len(grid[0])
        
        qu = []
        def bfs(r,c):
            qu.append([r,c])
            while qu:
                r,c=qu.pop(0)
                if (r,c) not in visited and grid[r][c]=='1':
                    visited.add((r,c))
                    if r!=0 and grid[r-1][c]=='1':#up
                        qu.append([r-1,c])
                    if r!=row-1 and grid[r+1][c]=='1':#down
                        qu.append([r+1,c])
                    if c!=0 and grid[r][c-1]=='1': #left
                        qu.append([r,c-1])
                    if c!=col-1 and grid[r][c+1]=='1':#right
                        qu.append([r,c+1])
        count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    count+=1
        return count