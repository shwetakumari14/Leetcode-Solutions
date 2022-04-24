class Solution:
    def stairsCount1(self, x):
        if x == 1:
            return 1
        result = [0 for i in range(x)]
        result[0],result[1] = 1, 2
        for i in range(2, x):
            result[i] = result[i-1] + result[i-2]
                
        return result[-1]
    
    def stairsCount2(self, x):
        if x == 1:
            return 1
        
        oneStep, twoStep = 1, 2
        for i in range(2, x):
            temp = twoStep
            twoStep = oneStep + twoStep
            oneStep = temp
                
        return twoStep


obj = Solution()
ans = obj.stairsCount2(5)
print(ans)