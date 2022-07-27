class Solution(object): #DFS
    def numIslands(self, grid):
        visited = set()
        queue = []
        rows, cols = len(grid), len(grid[0])
        islands = 0 
        
        def bfs(r,c):
            queue.append([r,c])
            while queue:
                r,c = queue.pop(0)
                if (r,c) not in visited:
                    visited.add((r,c))
                    if r - 1 >= 0 and grid[r-1][c] == '1':
                        queue.append([r-1,c])
                    if r + 1 < rows and grid[r+1][c] == '1':
                        queue.append([r+1,c])
                    if c - 1 >= 0 and grid[r][c-1] == '1':
                        queue.append([r,c-1])
                    if c+1 < cols and grid[r][c+1] == '1':
                        queue.append([r,c+1])
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1 
        return islands

