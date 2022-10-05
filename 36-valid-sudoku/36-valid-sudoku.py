class Solution(object):
    def isValidSudoku(self, board):
        rowContains = set()
        colContains = set()
        squares = defaultdict(set)
        for x in range(9):
            for y in range(9):
                if board[x][y] != ".":
                    if board[x][y] in rowContains or board[x][y] in squares[(x//3,y//3)]:
                        return False
                    else:
                        rowContains.add(board[x][y])
                        squares[(x//3,y//3)].add(board[x][y])
            
                if board[y][x] != ".":
                    if board[y][x] in colContains:
                        return False
                    else:
                        colContains.add(board[y][x])
              
                
            rowContains, colContains = set(),set()
        return True