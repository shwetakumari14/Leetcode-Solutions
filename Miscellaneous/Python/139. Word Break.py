class Solution:
    def wordBreak(self, s,  wordDict):
        wordSet = set(wordDict)
        n = len(s)
        dpArray = [False]*(n+1)
        dpArray[n] = True

        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if dpArray[j] and s[i:j] in wordSet:
                    dpArray[i] = True
                    break
        
        return dpArray[0]

     

obj = Solution()
s, wordDict = "applepenapple", ["apple","pen"]
ans = obj.wordBreak(s,  wordDict)
print(ans)
        