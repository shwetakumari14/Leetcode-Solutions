class Solution:
    def wordPattern(self, pattern, s):
        dict_pattern, dict_words = {}, {}

        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        for char, word in zip(pattern, words):
            if char not in dict_pattern:
                if word in dict_words:
                    return False
                else:
                    dict_pattern[char] = word
                    dict_words[word] = char
            else:
                if dict_pattern[char] != word:
                    return False
        
        return True
     

obj = Solution()
pattern, s = "abba", "dog cat cat dog"
ans = obj.wordPattern(pattern, s)
print(ans)
        