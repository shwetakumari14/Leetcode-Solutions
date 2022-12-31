class Solution:
    def uniquePaths(self, m, n):
        dpArray = [[1]*n for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dpArray[i][j] = dpArray[i-1][j] + dpArray[i][j-1]
        
        return dpArray[-1][-1]

        

obj = Solution()
n, m = 3, 7
ans = obj.uniquePaths(m, n)
print(ans)
                    