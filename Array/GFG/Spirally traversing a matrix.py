class Solution:
    def spiralMatrix(self, matrix, r, c):
        ans = []
  
        if (len(matrix) == 0):
            return ans
    
        seen = [[0 for i in range(r)] for j in range(r)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        x = 0
        y = 0
        di = 0
    
        for i in range(r * c):
            ans.append(matrix[x][y])
            seen[x][y] = True
            cr = x + dr[di]
            cc = y + dc[di]
    
            if (0 <= cr and cr < r and 0 <= cc and cc < c and not(seen[cr][cc])):
                x = cr
                y = cc
            else:
                di = (di + 1) % 4
                x += dr[di]
                y += dc[di]
        return ans

obj = Solution()
matrix, r, c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]], 4, 4
ans = obj.spiralMatrix(matrix, r, c)
print(ans)