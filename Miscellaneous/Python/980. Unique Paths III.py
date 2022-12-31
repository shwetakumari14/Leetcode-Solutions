class Solution:
    def uniquePathsIII(self, grid):
        rows, cols = len(grid), len(grid[0])

        noOfObs, st_row, st_col = 0, 0, 0

        for row in range(0, rows):
            for col in range(0, cols):
                cell = grid[row][col]
                if cell >= 0:
                    noOfObs += 1
                if cell == 1:
                    st_row, st_col = row, col

        path_count = 0

        def backtrack(row, col, remaining):
            nonlocal path_count

            if grid[row][col] == 2 and remaining == 1:
                path_count += 1
                return
            
            temp = grid[row][col]
            grid[row][col] = -4
            remaining -= 1

            for ro, co in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                next_row, next_col = row + ro, col + co

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                if grid[next_row][next_col] < 0:
                    continue

                backtrack(next_row, next_col, remaining)
            
            grid[row][col] = temp
        
        backtrack(st_row, st_col, noOfObs)

        return path_count
     

obj = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
ans = obj.uniquePathsIII(grid)
print(ans)
        