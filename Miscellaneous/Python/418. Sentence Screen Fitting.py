class Solution:
    def wordsTyping(self, sentence, rows, cols):
        n, wrdIdx, ans = len(sentence), 0, 0

        for _ in range(rows):
            cnt = 0
            while cnt + len(sentence[wrdIdx]) <= cols:
                cnt += len(sentence[wrdIdx]) + 1
                wrdIdx += 1

                if wrdIdx == n:
                    wrdIdx = 0
                    ans += 1
        
        return ans
    
    def wordsTypingOptimized(self, sentence, rows, cols):
        n = len(sentence)

        def dp(i):
            cnt, times = 0, 0
            while cnt + len(sentence[i]) <= cols:
                cnt += len(sentence[i]) + 1
                i += 1

                if i == n:
                    i = 0
                    times += 1
                
            return i, times
        
        ans, wrdIdx = 0, 0

        for _ in range(rows):
            ans += dp(wrdIdx)[1]
            wrdIdx = dp(wrdIdx)[0]
        
        return ans
    



obj = Solution()
sentence, rows, cols = ["a", "bcd", "e"], 3, 6
ans = obj.wordsTypingOptimized(sentence, rows, cols)
print(ans)
        