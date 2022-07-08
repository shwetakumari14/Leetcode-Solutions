class Solution:
    def stockBuySell (self, arr, n):
        maxLen, initial = 0, arr[0]

        for i in range(1, len(arr)):
            profit = arr[i] - initial
            maxLen = max(profit, profit)
            initial = min(initial, arr[i])
        
        if maxLen == 0:
            return 0
        
        return 1

obj = Solution()
arr, n = [100,180,260,310,40,535,695], 7
ans = obj.stockBuySell(arr, n)
print(ans)