class Solution:
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)

        if n * m == 0:
            return n + m
        
        dpArray = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(n+1):
            dpArray[i][0] = i
        
        for j in range(m+1):
            dpArray[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                left = dpArray[i-1][j] + 1
                down = dpArray[i][j-1] + 1
                leftDown = dpArray[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    leftDown += 1
                dpArray[i][j] = min(left, down, leftDown)
        
        return dpArray[n][m]



obj = Solution()
word1, word2 = "intention",  "execution" 
ans = obj.minDistance(word1, word2)
print(ans)
        