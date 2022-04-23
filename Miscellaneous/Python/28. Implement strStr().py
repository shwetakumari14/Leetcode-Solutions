class Solution:
    def strStr(self, haystack, needle):
        counter = 0
        index = -1

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

obj = Solution()
haystack, needle = "hello", "ll"
ans = obj.strStr(haystack, needle)
print(ans)

def KMPSearch(pat, txt):
        m,n, i, j = len(pat), len(txt), 0, 0

        lps = [0]*m

        prepareLPS(pat, m, lps)

        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            
            if j == m:
                print("Pattern found at ", str(i-j))
                j = lps[j-1]
            
            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j= lps[j-1]
                else:
                    i += 1
    
def prepareLPS(pat, m, lps):
    len = 0
    lps[0]=0
    i=1

    while i < m:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += i
        
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1


txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)