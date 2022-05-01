class Solution:
   def hammingWeight(self, n):
        res = 0

        for i in range(32):
            res += (n&1)
            n >>= 1

        return res

obj = Solution()
n = 11111111111111111111111111111101
ans = obj.hammingWeight(n)
print(ans)