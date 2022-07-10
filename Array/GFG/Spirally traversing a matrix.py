class Solution:
    def spiralMatrix(self, matrix, r, c):
        ans, k = [], 0

        stRow, endRow, stCol, endCol = 0, r-1, 0, c-1

        while stRow <= endRow and stCol <= endCol:

            for i in range(stCol, endCol+1):
                ans.append(matrix[stRow][i])
            stRow += 1

            for i in range(stRow, endRow+1):
                ans.append(matrix[i][endCol])
            endCol -= 1

            for i in range(endCol, stCol-1, -1):
                ans.append(matrix[endRow][i])
            endRow -= 1

            for i in range(endRow, stRow-1, -1):
                ans.append(matrix[i][stCol])
            stCol += 1

        return ans

obj = Solution()
matrix, r, c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]], 4, 4
ans = obj.spiralMatrix(matrix, r, c)
print(ans)