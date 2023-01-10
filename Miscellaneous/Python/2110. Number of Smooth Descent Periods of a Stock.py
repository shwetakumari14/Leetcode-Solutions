class Solution:
    def getDescentPeriods(self, prices):
        result, temp = 1, 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                temp += 1
            else:
                temp = 1
            
            result += temp
        
        return result


obj = Solution()
prices = [3,2,1,4]
ans = obj.getDescentPeriods(prices)
print(ans)