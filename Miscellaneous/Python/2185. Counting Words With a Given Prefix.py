class Solution:
    def prefixCount(self, words, pref):
        count = 0

        for char in words:
            if char.startswith(pref):
                count += 1
        
        return count

     

obj = Solution()
words, pref = ["pay","attention","practice","attend"], "at"
ans = obj.prefixCount(words, pref)
print(ans)
        