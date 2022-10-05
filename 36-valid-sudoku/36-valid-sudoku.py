class Solution(object):
    def isValidSudoku(self, board):
        rowContains = defaultdict(set)
        colContains = defaultdict(set)
        squares = defaultdict(set)
        for x in range(9):
            for y in range(9):
                value = board[x][y]
                if value != ".":
                    if value in rowContains[x] or value in colContains[y] or value in squares[(x//3,y//3)]:
                        return False
                    else:
                        rowContains[x].add(value)
                        colContains[y].add(value)
                        squares[(x//3,y//3)].add(value)
        return True