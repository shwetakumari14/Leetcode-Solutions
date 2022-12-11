class Solution:
    def exist(self, board, word):
        self.row = len(board)
        self.col = len(board[0])
        self.board = board

        for i in range(self.row):
            for j in range(self.col):
                if self.wordFound(i, j, word):
                    return True
        
        return False

    def wordFound(self, row, col, suffix):
        if len(suffix) == 0:
            return True
        
        if row < 0 or row == self.row or col < 0 or col == self.col or self.board[row][col] != suffix[0]:
            return False
        
        self.board[row][col] = "#"

        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if self.wordFound(row + rowOffset, col + colOffset, suffix[1:]):
                return True
        
        self.board[row][col] = suffix[0]

        return False
    
        


obj = Solution()
board, word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
ans = obj.exist(board, word)
print(ans)
        