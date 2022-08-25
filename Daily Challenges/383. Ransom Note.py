class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        
        for char in magazine:
            if char not in dict.keys():
                dict[char] = 1
            else:
                dict[char] += 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] not in dict.keys():
                return False
            elif dict[ransomNote[i]] < 1:
                return False
            else:
                dict[ransomNote[i]] -= 1
        
        return True

obj = Solution()
ransomNote, magazine = "aa", "aab"
ans = obj.canConstruct(ransomNote, magazine)
print(ans)