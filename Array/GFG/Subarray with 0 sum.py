class Solution:
    def zeroSum(self, arr, n):
        ans, sum = set(), 0

        for i in range(n):
            sum += arr[i]

            if sum == 0 or sum in ans:
                return True
            ans.add(sum)

        return False

obj = Solution()
arr, n = [4, 2, -3, 1, 6], 5
ans = obj.zeroSum(arr, n)
print(ans)