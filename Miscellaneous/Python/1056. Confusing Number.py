class Solution:
    def confusingNumber(self, n):
        validDigits = {0:0, 1:1, 8:8, 6:9, 9:6}
        newNum, temp = 0, n

        while temp > 0:
            rem = temp % 10
            if rem not in validDigits:
                return False
            
            newNum = newNum*10 + validDigits[rem]
            temp = temp // 10
        
        return newNum != n
     

obj = Solution()
n = 8
ans = obj.confusingNumber(n)
print(ans)
        