class Solution:
    def uniqueChar(self, str):
        dict = {}

        for char in str:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        
        
        for i in range(len(str)):
            if dict[str[i]] == 1:
                return i
        
        return -1

obj = Solution()
str = "loveleetcode"
ans = obj.uniqueChar(str)
print(ans)