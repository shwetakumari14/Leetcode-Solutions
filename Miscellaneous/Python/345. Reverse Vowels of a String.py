class Solution:
    def reverseVowels(self, s):
        str = list(s)
        low, high = 0, len(str)-1

        while low < high:
            while low < high and str[low] not in "aeiouAEIOU": low += 1
            while low < high and str[high] not in "aeiouAEIOU": high -= 1
            str[low], str[high] = str[high], str[low]
            low += 1
            high -= 1
        
        return ''.join(str)

     

obj = Solution()
s = "leetcode"
ans = obj.reverseVowels(s)
print(ans)
        