class Solution:
    def calculateTime(self, keyboard, word):
        alphaPos = [0 for i in range(26)]

        for i, key in enumerate(keyboard):
            alphaPos[ord(key) - ord('a')] = i
        
        prev, result = 0, 0

        for char in word:
            result += abs(alphaPos[ord(char) - ord('a')] - prev)
            prev = alphaPos[ord(char) - ord('a')]


        return result

     

obj = Solution()
keyboard, word = "pqrstuvwxyzabcdefghijklmno","leetcode"
ans = obj.calculateTime(keyboard, word)
print(ans)
        