class Solution:
    def spiralOrder(self, matrix):
        self.transpose(matrix)
        self.rotateClockwise(matrix)
        #self.rotateAntiClockwise(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def rotateClockwise(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][i]
    
    def rotateAntiClockwise(self, matrix):
        n = len(matrix)

        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[-i-1][j] = matrix[-i-1][j], matrix[i][j]
        


obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj.spiralOrder(matrix)
print(matrix)
        