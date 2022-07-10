class Solution:
    def zeroSum(self, arr, n):
        left, right, ans = [0]*n, [0]*n, 0
        left[0], right[n-1] = arr[0], arr[n-1]

        for i in range(1, n):
            left[i] = max(left[i-1], arr[i])
                
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
        
        
        for i in range(n):
            ans += min(left[i], right[i]) - arr[i]

        return ans

obj = Solution()
arr, n = [3,0,0,2,0,4], 6
ans = obj.zeroSum(arr, n)
print(ans)