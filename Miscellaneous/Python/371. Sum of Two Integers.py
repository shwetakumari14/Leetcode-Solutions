class Solution:
    def getSum(self, a, b):
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1

        if a*b >= 1:
            while y:
                ans = x ^ y
                carry = (x & y) << 1
                x, y = ans, carry
        else:
            while y:
                ans = x ^ y
                carry = ((~x) & y) << 1
                x, y = ans, carry
        
        return x * sign

obj = Solution()
a, b = 243, 897
ans = obj.getSum(a, b)
print(ans)
        