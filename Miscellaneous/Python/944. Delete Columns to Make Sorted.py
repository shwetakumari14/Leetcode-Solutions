class Solution:
    def minDeletionSize(self, strs):
        n, m, result = len(strs), len(strs[0]), 0

        for col in range(m):
            found = False
            for row in range(1, n):
                if strs[row][col] < strs[row-1][col]:
                    result += 1
                    break
        
        return result

obj = Solution()
strs = ["zyx","wvu","tsr"]
ans = obj.minDeletionSize(strs)
print(ans)