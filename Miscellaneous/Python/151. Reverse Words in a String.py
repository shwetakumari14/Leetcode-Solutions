class Solution:
    def reverseWords(self, words):
        
        temp = words.split()

        return " ".join(reversed(temp))


obj = Solution()
words = "the sky is blue"
ans = obj.reverseWords(words)
print(ans)