class Solution:
    def maxIceCream(self, costs, coins):
        costs.sort()

        icecream, n = 0, len(costs)

        while icecream < n and costs[icecream] <= coins:
            coins -= costs[icecream]
            icecream += 1
        
        return icecream


obj = Solution()
costs, coins = [1,6,3,1,2,5],  20
ans = obj.maxIceCream(costs, coins)
print(ans)