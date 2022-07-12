class Solution:
    def maxOnesRow(self,arr, n, m):
        i, j, ans = 0, m-1, -1

        while i < n:
            while j >= 0 and arr[i][j] == 1:
                ans = i
                j -= 1
            i += 1

        return ans

obj = Solution()
arr, n, m = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]], 4, 4
ans = obj.maxOnesRow(arr, n, m)
print(ans)