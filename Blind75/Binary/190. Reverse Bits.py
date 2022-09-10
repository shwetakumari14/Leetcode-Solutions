class Solution:
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            res = (res << 1) + n&1
            n >>= 1

        return res


obj = Solution()
n = 10000000000000000000000000000011
ans = obj.reverseBits(n)
print(ans)