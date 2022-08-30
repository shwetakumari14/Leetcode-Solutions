class Solution:
    def setZeroes(self, matrix):
        r, c = len(matrix), len(matrix[0])
        row = [False for i in range(r)]
        col = [False for i in range(c)]
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        
        for i in range(r):
            for j in range(c):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        
        return matrix

obj = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
ans = obj.setZeroes(matrix)
print(ans)