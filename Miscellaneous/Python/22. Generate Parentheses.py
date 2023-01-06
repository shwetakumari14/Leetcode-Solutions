class Solution:
    def generateParenthesis(self, n):
        result = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2*n:
                result.append(''.join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        
        backtrack()
        return result


obj = Solution()
n = 3
ans = obj.generateParenthesis(n)
print(ans)