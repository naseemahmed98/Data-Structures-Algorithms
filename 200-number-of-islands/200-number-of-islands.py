from collections import deque
class Solution(object): #BFS
    def numIslands(self, grid):
        visited = set()
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        num_islands = 0 
        
        def bfs(x,y):
            queue.append((x,y))
            while queue:
                x,y = queue.popleft()
                if (x,y) not in visited:
                    visited.add((x,y))
                    if x+1 < rows and grid[x+1][y] == '1':
                        queue.append((x+1,y))
                    if x-1 >= 0 and grid[x-1][y] == '1':
                        queue.append((x-1,y))
                    if y+1 < cols and grid[x][y+1] == '1':
                        queue.append((x,y+1))
                    if y-1 >= 0 and grid[x][y-1] == '1':
                        queue.append((x,y-1))
        
        
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1' and (x,y) not in visited:
                    num_islands += 1 
                    bfs(x,y)

        return num_islands