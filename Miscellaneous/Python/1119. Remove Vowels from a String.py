class Solution:
    def removeVowels(self, s):
        result = ""

        for char in s:
            if char not in "aeiouAEIOU":
                result += char
        
        return result

     

obj = Solution()
s = "leetcodeisacommunityforcoders"
ans = obj.removeVowels(s)
print(ans)
        