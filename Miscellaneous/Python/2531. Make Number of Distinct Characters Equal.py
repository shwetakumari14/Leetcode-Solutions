import collections

class Solution:
    def maxKelements(self, word1, word2):
        d1 = collections.Counter(word1)
        d2 = collections.Counter(word2)

        for ch, cnt1 in d1.items():
            for ch2, cnt2 in d2.items():
                if ch == ch2:
                    if len(d1) == len(d2):
                        return True
                else:
                    l1 = len(d1)
                    if cnt1 == 1:
                        l1 -= 1
                    if d1[ch2] == 0:
                        l1 += 1
                    l2 = len(d2)
                    if cnt2 == 1:
                        l2 -= 1
                    if d2[ch] == 0:
                        l2 += 1
                    if l1 == l2:
                        return True
        
        return False


obj = Solution()
word1, word2 = "abcc", "aab"
ans = obj.maxKelements(word1, word2)
print(ans)