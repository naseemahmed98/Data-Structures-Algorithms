class Solution(object):
    def setZeroes(self, matrix):
  
        zeroRow = set()
        zeroCol = set()
        
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRow.add(i)
                    zeroCol.add(j)
        for i in range(m):
            for j in range(n):
                if i in zeroRow or j in zeroCol:
                    matrix[i][j] = 0 
        
        return matrix
