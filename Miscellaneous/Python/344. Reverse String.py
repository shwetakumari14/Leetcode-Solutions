class Solution:
    def reverseString(self, str):
        i, j = 0, len(str)-1

        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
        
        return str

obj = Solution()
str = ["H","a","n","n","a","h"]
ans = obj.reverseString(str)
print(ans)