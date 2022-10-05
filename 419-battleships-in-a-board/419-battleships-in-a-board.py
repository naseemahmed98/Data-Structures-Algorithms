class Solution(object):
    def countBattleships(self, board):
        
        def dfs(x,y):
            board[x][y] = '.'
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for a,b in directions: 
                if 0 <= x+a < rows and 0 <= y + b < cols and board[x+a][y+b] == 'X':
                    dfs(x+a,y+b)
                    
    
        rows, cols = len(board),len(board[0])
        numShips = 0 
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 'X':
                    dfs(x,y)
                    numShips += 1 
        return numShips 