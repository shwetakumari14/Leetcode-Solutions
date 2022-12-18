class Solution:
    def longestCommonPrefix(self, strs):
        prefix = []

        for char in zip(*strs):
            if len(set(char)) == 1:
                prefix.append(char[0])
            else:
                break
        
        return ''.join(prefix)

     

obj = Solution()
strs = ["flower","flow","flight"]
ans = obj.longestCommonPrefix(strs)
print(ans)
        