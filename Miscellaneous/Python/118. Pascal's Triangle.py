class Solution:
    def generate(self, numRows):
        sol = [[1]*(i+1) for i in range(numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                sol[i][j] = sol[i-1][j-1] + sol[i-1][j]

        return sol

obj = Solution()
ans = obj.generate(5)
print(ans)