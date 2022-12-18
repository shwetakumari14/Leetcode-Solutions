class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1

        for i in range(1, n):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
        
        for j in range(1, m):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[n-1][m-1]

     

obj = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
ans = obj.uniquePathsWithObstacles(obstacleGrid)
print(ans)
        