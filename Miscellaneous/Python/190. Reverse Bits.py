class Solution:
   def reverseBits(self, n):
        ans = 0
        
        for i in range(32):
            ans = (n&1) + ans << 1
            n = n>>1

        return ans

obj = Solution()
n = 10000010100101000001111010011100
ans = obj.reverseBits(n)
print(ans)