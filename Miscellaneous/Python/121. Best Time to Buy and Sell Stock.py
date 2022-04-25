class Solution:
    def maxProfit(self, prices):
        maxDiff, initial = 0, prices[0]

        for i in range(1, len(prices)):
            profit = prices[i] - initial
            maxDiff = max(maxDiff, profit)
            initial = min(initial, prices[i])

        return maxDiff

obj = Solution()
prices = [7,1,5,3,6,4]
ans = obj.maxProfit(prices)
print(ans)