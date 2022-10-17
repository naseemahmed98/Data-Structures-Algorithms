class Solution(object):
    def gameOfLife(self, board):
        rows, cols = len(board), len(board[0])
        nextState = [[0 for x in range(cols)] for y in range(rows)]
        directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        for x in range(rows):
            for y in range(cols):
                counter = 0 
                for a,b in directions:
                    if 0 <= x + a < rows and 0 <= y + b < cols and board[x+a][y+b] == 1:
                        counter += 1 
                if board[x][y] == 1:
                    if counter > 3 or counter < 2:
                        nextState[x][y] = 0 
                    else:
                        nextState[x][y] = 1
        
                else:
                    if counter == 3:
                        nextState[x][y] = 1 
                    else:
                        nextState[x][y] = 0 
        print(nextState)
        for x in range(rows):
            for y in range(cols):
                board[x][y] = nextState[x][y]
        
                
                