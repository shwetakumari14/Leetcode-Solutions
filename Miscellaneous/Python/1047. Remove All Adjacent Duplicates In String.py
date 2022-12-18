class Solution:
    def removeDuplicates(self, s):
        output = []

        for char in s:
            if output and output[-1] == char:
                output.pop()
            else:
                output.append(char)
        
        return ''.join(output)
     

obj = Solution()
s = "azxxzy"
ans = obj.removeDuplicates(s)
print(ans)
        