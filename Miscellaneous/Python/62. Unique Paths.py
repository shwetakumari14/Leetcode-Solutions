class Solution:
    def uniquePaths(self, p, q):
        m, n = int(p), int(q)
        dp = [1 for i in range(n)]

        for i in range(m-1):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[n-1]

        

obj = Solution()
n, m = "3", "3"
ans = obj.uniquePaths(m, n)
print(ans)
                    