class Solution:
    def plusOne(self, digits):
        ans, carry = [], 1

        for i in range(len(digits)-1, -1, -1):
            sum = digits[i] + carry
            carry = sum // 10
            ans.append(sum % 10)
            sum  = 0

        if carry > 0:
            ans.append(carry)

        ans.reverse()

        return ans

obj = Solution()
digits = [1,2,3]
ans = obj.plusOne(digits)
print(ans)