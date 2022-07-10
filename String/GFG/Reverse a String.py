class Solution:
    def reverseString(self, str):
        str = str[::-1]
       

        return str

obj = Solution()
str = "Geeks"
ans = obj.reverseString(str)
print(ans)