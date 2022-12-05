class Solution:
    def longestLine(self, matrix):
        n, m, onesLen = len(matrix), len(matrix[0]), 0
        dpArray = [[[0 for i in range(4)] for j in range(m)] for k in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    if j > 0:
                        dpArray[i][j][0] = dpArray[i][j-1][0] + 1
                    else:
                        dpArray[i][j][0] = 1
                    if i > 0:
                        dpArray[i][j][1] = dpArray[i-1][j][1] + 1
                    else:
                        dpArray[i][j][1] = 1
                    if i > 0 and j > 0:
                        dpArray[i][j][2] = dpArray[i-1][j-1][2] + 1
                    else:
                        dpArray[i][j][2] = 1
                    if i > 0 and j < m-1:
                        dpArray[i][j][3] = dpArray[i-1][j+1][3] + 1
                    else:
                        dpArray[i][j][3] = 1
                    
                    onesLen = max(onesLen, max(dpArray[i][j][0], dpArray[i][j][1], dpArray[i][j][2], dpArray[i][j][3]))
        
        return onesLen

obj = Solution()
matrix = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
ans = obj.longestLine(matrix)
print(ans)
        