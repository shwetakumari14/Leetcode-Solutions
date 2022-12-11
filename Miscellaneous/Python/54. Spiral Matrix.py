class Solution:
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        up, down, left, right, ans = 0, rows - 1, 0, cols - 1, []

        while len(ans) < rows * cols:

            for i in range(left, right+1):
                ans.append(matrix[up][i])
            
            for i in range(up + 1, down + 1):
                ans.append(matrix[i][right])
            
            if up != down:
                for i in range(right - 1, left - 1, -1):
                    ans.append(matrix[down][i])
            
            if left != right:
                for i in range(down - 1, up, -1):
                    ans.append(matrix[i][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return ans
        


obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = obj.spiralOrder(matrix)
print(ans)
        