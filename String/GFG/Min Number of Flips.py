from itertools import count


class Solution:            
    def minFlip(self, S):
        cnt1, cnt2 = 0, 0

        for i in range(len(S)):
            if i%2 == 0 and S[i] == '1':
                cnt1 += 1
            if i%2 == 0 and S[i] == '0':
                cnt2 += 1
            if i%2 and S[i] == '0':
                cnt1 += 1
            if i%2 and S[i] == '1':
                cnt2 += 1
            
        return min(cnt1, cnt2)

obj = Solution()
S = "0001010111"
ans = obj.minFlip(S)
print(ans)