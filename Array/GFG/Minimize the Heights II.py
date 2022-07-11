class Solution:
    def minimizeTowerHeight(self, arr, n, k):        
        arr.sort()

        ans, minimum, maximum = arr[n-1]-arr[0], arr[0], arr[n-1]
        
        for i in range(1, n):
            if arr[i] >= k:
                minimum, maximum = min(arr[0]+k, arr[i]-k), max(arr[i-1]+k, arr[n-1]-k)
                ans = min(ans, maximum-minimum)        
        return ans

obj = Solution()
arr, n, k = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1], 10, 5
ans = obj.minimizeTowerHeight(arr, n, k)
print(ans)