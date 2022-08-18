class Solution(object):
    def countBattleships(self, board):
        
        rows, cols = len(board), len(board[0])
        
        num_ships = 0 
        
        def dfs(x,y):
            
            board[x][y] = "."
            if x+1 < rows and board[x+1][y] == "X":
                dfs(x+1,y)
            if x-1 >= 0 and board[x-1][y] == "X":
                dfs(x-1,y)
            if y+1 < cols and board[x][y+1] == "X":
                dfs(x,y+1)
            if y-1 >= 0 and board[x][y-1] == "X":
                dfs(x,y-1)
        
        
        
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "X":
                    dfs(x,y)
                    num_ships += 1 
        
        return num_ships
                    