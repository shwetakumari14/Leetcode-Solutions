class Solution:
    def maxAreaOfIsland(self, grid):
        row, col = len(grid), len(grid[0])
        seen = set()

        def area(r, c):
            if not (0 <= r < row and 0 <= c < col and (r,c) not in seen and grid[r][c]):
                return 0
            
            seen.add((r, c))

            return (1 + area(r+1, c) + area(r-1, c) + area(r, c+1) +  area(r, c-1))
        
        return max(area(r, c) for r in range(row) for c in range(col))
        
     

obj = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
ans = obj.maxAreaOfIsland(grid)
print(ans)
        