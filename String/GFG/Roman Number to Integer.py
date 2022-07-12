class Solution:            
    def romanToDecimal(self, S):
            romans = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            }
            
            num, total, i, n = 0, 0, 0, len(S)
            
            while i < n:
                if i == n-1 or romans[S[i]] >= romans[S[i+1]]:
                    num = romans[S[i]]
                    i += 1
                else:
                    num = romans[S[i+1]] - romans[S[i]]
                    i += 2
                
                total += num
            
            return total

obj = Solution()
S = "CMXVI"
ans = obj.romanToDecimal(S)
print(ans)