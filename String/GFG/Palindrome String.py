class Solution:
    def palindromeString(self, s):
        n = len(s)

        for i in range(n):
            if s[i] != s[n-1-i]:
                return 0

        return 1

obj = Solution()
str = "abba"
ans = obj.palindromeString(str)
print(ans)