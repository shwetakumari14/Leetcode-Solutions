class Solution:
    def maxProfit(self, prices):
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]

        return maxProfit

obj = Solution()
prices = [1,2,3,4,5]
ans = obj.maxProfit(prices)
print(ans)
        