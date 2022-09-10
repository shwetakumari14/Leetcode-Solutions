class Solution:
    def countingBits(self, n):
        setBits = [0]*(n+1)

        for i in range(1, n+1):
            setBits[i] = setBits[i & (i-1)] + 1
        
        return setBits


obj = Solution()
n = 5
ans = obj.countingBits(n)
print(ans)