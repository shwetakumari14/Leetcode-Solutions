from collections import Counter

class Solution:
    def robotWithString(self, s):
        result, t, dict = [], [], Counter(s)

        for char in s:
            t.append(char)
            if dict[char] == 1:
                del dict[char]
            else:
                dict[char] -= 1
            
            while dict and t and t[-1] <= min(dict):
                result += t.pop()
        
        result += t[::-1]

        return ''.join(result)

obj = Solution()
s = "zza"
ans = obj.robotWithString(s)
print(ans)