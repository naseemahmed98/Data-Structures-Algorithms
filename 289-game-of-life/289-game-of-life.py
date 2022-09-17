class Solution(object):
    def gameOfLife(self, board):
        rows, cols = len(board), len(board[0])
        ones = set()
        nextState = [[0 for x in range(cols)] for y in range(rows)]
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == 1:
                    ones.add((x,y))
        
        neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for x in range(rows):
            for y in range(cols):
                neighborOnes = 0 
                for a,b in neighbors:
                    if 0 <= (x+a) < rows and 0 <=(y+b) < cols and board[x+a][y+b] == 1:
                        neighborOnes += 1 
                if board[x][y] == 1:
                    if neighborOnes < 2 or neighborOnes > 3:
                        nextState[x][y] = 0
                    elif 2 <= neighborOnes <=3:
                        nextState[x][y] = 1
                elif board[x][y] == 0:
                    if neighborOnes == 3:
                        nextState[x][y] = 1 
        for x in range(rows):
            for y in range(cols):
                board[x][y] = nextState[x][y]
        