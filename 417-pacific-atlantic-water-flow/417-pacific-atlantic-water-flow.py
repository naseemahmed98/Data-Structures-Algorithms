class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        
        pac,atl = set(),set()
        
        def dfs(x, y, _set_, prev):
            if x >= rows or y >= cols or x < 0 or y < 0 or heights[x][y] < prev or (x,y) in _set_:
                return
            _set_.add((x,y))
            node = heights[x][y]
            dfs(x+1,y,_set_,node)
            dfs(x-1,y,_set_,node)
            dfs(x,y+1,_set_,node)
            dfs(x,y-1,_set_,node)
        
        for z in range(cols):
            dfs(0, z, pac,0)
            dfs(rows-1,z,atl,0)
        
        for z in range(rows):
            dfs(z,0,pac,0)
            dfs(z,cols-1,atl,0)
            
        return pac & atl