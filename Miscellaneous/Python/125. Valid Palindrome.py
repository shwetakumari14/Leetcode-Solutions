class Solution:
    def isPalindrome(self, s):
        string = ''.join(filter(str.isalnum, s))
        string = string.lower()
        n = len(string)

        for i in range(n):
            if string[i] != string[n-1-i]:
                return False

        return True

obj = Solution()
s = "A man, a plan, a canal: Panama"
ans = obj.isPalindrome(s)
print(ans)