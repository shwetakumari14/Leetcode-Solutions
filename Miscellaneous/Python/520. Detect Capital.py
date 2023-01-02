class Solution:
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower() or word.istitle():
            return True
        
        return False
     

obj = Solution()
word = "USA"
ans = obj.detectCapitalUse(word)
print(ans)
        