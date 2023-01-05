class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        aliceSum, bobSum = sum(aliceSizes), sum(bobSizes)
        bobSet = set(bobSizes)

        for x in aliceSizes:
            if x + (bobSum - aliceSum)//2 in bobSet:
                return [x, x + (bobSum - aliceSum)//2]


obj = Solution()
aliceSizes, bobSizes = [1,2], [2,3]
ans = obj.fairCandySwap(aliceSizes, bobSizes)
print(ans)