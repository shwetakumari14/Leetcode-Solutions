class Solution:
    def isValidAnagram(self, str1, str2):

        if len(str1) is not len(str2):
            return False

        count = 0

        for char in str1:
            count += ord(char)

        for char in str2:
            count -= ord(char)

        if count == 0:
            return True
        return False

obj = Solution()
s, t = "anagram", "nagaram"
ans = obj.isValidAnagram(s, t)
print(ans)