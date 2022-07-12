class Solution:            
    def countRev(self, s):
        revCount, open = 0,  0
        
        if len(s) % 2:
            return -1
        
        for char in s:
            if char == "{":
                open += 1
            else:
                open -= 1
            
            if open == -1:
                revCount += 1
                open = 1
        
        return revCount + (open//2)

obj = Solution()
S = "}{{}}{{{"
ans = obj.countRev(S)
print(ans)