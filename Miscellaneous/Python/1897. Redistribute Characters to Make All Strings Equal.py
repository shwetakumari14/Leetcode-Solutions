class Solution:
    def makeEqual(self, words):
        alphaMap = {}

        for word in words:
            for char in word:
                if char not in alphaMap:
                    alphaMap[char] = 1
                else:
                    alphaMap[char] += 1
        
        n = len(words)

        for _, val in alphaMap.items():
            if (val % n) != 0:
                return False
        
        return True


obj = Solution()
words = ["abc","aabc","bc"]
ans = obj.makeEqual(words)
print(ans)