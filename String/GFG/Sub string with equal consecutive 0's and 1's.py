class Solution:
    def countSubstrings(self, str):

        i, ans, n = 0 , 0, len(str)
        while i < n:
            cnt0, cnt1 = 0 , 0
            if str[i] == '0':
                while i < n and str[i] == '0':
                    cnt0 += 1
                    i += 1

                j = i

                while j < n and str[j] == '1':
                    cnt1 += 1
                    j += 1
            else:
                while i < n and str[i] == '1':
                    cnt1 += 1
                    i += 1

                j = i

                while j < n and str[j] == '0':
                    cnt0 += 1
                    j += 1
            
            ans += min(cnt0, cnt1)

        return ans

obj = Solution()
str = "010011"
ans = obj.countSubstrings(str)
print(ans)
