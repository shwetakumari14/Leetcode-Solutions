from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False
        
        wordsSet = defaultdict(set)
        
        for word1, word2 in similarPairs:
            wordsSet[word1].add(word2)
            wordsSet[word2].add(word1)
        
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wordsSet[sentence1[i]]:
                continue
            return False
        
        return True

obj = Solution()
sentence1, sentence2, similarPairs = ["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]
ans = obj.areSentencesSimilar(sentence1, sentence2, similarPairs)
print(ans)