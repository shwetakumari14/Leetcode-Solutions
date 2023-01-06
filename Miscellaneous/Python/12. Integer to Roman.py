class Solution:
    def intToRoman(self, num):
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        result = []

        for value, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, value)
            result.append(count*symbol)
        
        return ''.join(result)


obj = Solution()
num = 1994
ans = obj.intToRoman(num)
print(ans)