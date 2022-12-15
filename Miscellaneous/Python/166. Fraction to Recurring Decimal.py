class Solution:
    def fractionToDecimal(self, numerator, denominator):
        num, remainder = divmod(abs(numerator), abs(denominator))
        sign = "-" if numerator * denominator < 0 else ""
        ans = sign + str(num)
        if remainder == 0:
            return ans
        
        remainderMap, decimal, i = {}, "", 0

        while remainder > 0 and remainder not in remainderMap:
            remainderMap[remainder] = i
            num, remainder = divmod(remainder*10, abs(denominator))
            decimal += str(num)
            i += 1
        
        if remainder in remainderMap:
            i = remainderMap[remainder]
            return ans + "." + decimal[:i] + "(" + decimal[i:] + ")"
        else:
            return ans + "." + decimal[:]

obj = Solution()
numerator, denominator = 4, 333
ans = obj.fractionToDecimal(numerator, denominator)
print(ans)
        