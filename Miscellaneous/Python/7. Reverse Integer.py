class Solution:
    def reverseInteger(self, x):
        number, temp = 0, abs(x)

        while temp > 0:
            rem = temp % 10
            number = number*10 + rem
            temp = temp // 10
        
        if x > 0 and number < 2**31:
            return number
        if x < 0 and number <= 2**31:
            return -number
        
        return 0

obj = Solution()
x = -123
ans = obj.reverseInteger(x)
print(ans)