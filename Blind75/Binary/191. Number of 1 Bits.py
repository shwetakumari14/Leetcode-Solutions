class Solution:
    def noOfBitOne(self, n):
        res = 0

        for i in range(32):
            res = res +(n&1)
            n >>= 1

        return res


obj = Solution()
n = 11111111111111111111111111111101
ans = obj.noOfBitOne(n)
print(ans)