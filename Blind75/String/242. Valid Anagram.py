class Solution:
    def isAnagram(sefl, str,rts):
        alphabets = [0]*26

        for i in range(len(str)):
            alphabets[ord(str[i]) - ord('a')] += 1
        
        for i in range(len(rts)):
            alphabets[ord(rts[i]) - ord('a')] -= 1

        for i in range(len(alphabets)):
            if alphabets[i] != 0:
                return False
        
        return True

obj = Solution()
str,rts = "anagram", "nagaram"
ans = obj.isAnagram(str,rts)
print(ans)