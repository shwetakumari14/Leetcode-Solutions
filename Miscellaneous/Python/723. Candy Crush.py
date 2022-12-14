class Solution:
    def candyCrush(self, board):
        row, col, toDo = len(board), len(board[0]), False

        for i in range(row):
            for j in range(col-2):
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]) != 0:
                    board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])
                    toDo = True
        
        for i in range(row-2):
            for j in range(col):
                if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]) != 0:
                    board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
                    toDo = True
        
        for c in range(col):
            wr = row-1
            for r in range(row-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
        
        return self.candyCrush(board) if toDo else board



obj = Solution()
board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
ans = obj.candyCrush(board)
print(ans)
        