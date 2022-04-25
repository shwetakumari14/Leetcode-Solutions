class Solution:
    def romanToInt(self, s):
        romans = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        }

        res = 0
        for i in range(len(s)):
            str1 = romans[s[i]]
            if i+1 < len(s):
                str2 = romans[s[i+1]]
                if str1 >= str2:
                    res += str1
                else:
                    res += str2
                    res -= str1
                    i=i+1
            else:
                res += str1

        return res

ans = Solution()
print(ans.romanToInt("XIX"))