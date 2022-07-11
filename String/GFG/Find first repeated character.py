class Solution:
    def firstRepeatedChar(self, s):
        dict = {}
        
        for char in s:
            if char in dict :
                return char
            else:
                dict[char] = 0

        return -1

obj = Solution()
s = "geeksforgeeks"
ans = obj.firstRepeatedChar(s)
print(ans)