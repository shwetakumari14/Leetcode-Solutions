class Solution:
    def maxProfit(self, prices):
        maxLen, itr = 0, prices[0]
        
        for i in range(1, len(prices)):
            profit = prices[i] - itr
            maxLen = max(maxLen, profit)
            itr = min(itr, prices[i])
        
        return maxLen

obj = Solution()
arr = [7,1,5,3,6,4]
ans = obj.maxProfit(arr)
print(ans)