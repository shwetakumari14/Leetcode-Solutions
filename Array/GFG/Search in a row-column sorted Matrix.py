class Solution:
    def searchInMatrix(self, arr, n, m, x):
        i, j = 0, m-1

        while i<n and j>=0:
            if arr[i][j] == x:
                return True
            if arr[i][j] > x:
                j -= 1
            else:
                i += 1

        return False

obj = Solution()
arr, n, m, x = [[3, 30, 38], [36, 43, 60], [40, 51, 69]], 3, 3, 62
ans = obj.searchInMatrix(arr, n, m, x)
print(ans)