class Solution:
    def KLenUniqueSubsequence(self, str, k):
        left, right = 0, -1
        dict, ans = {}, 0

        while right < len(str) -1:
            if right - left + 1 == k:
                ans += 1
                dict[str[left]] -= 1
                left += 1
            if str[right+1] not in dict:
                dict[str[right+1]] = 1
                right += 1
            elif not dict[str[right+1]]:
                dict[str[right+1]] += 1
                right += 1
            else:
                dict[str[left]] -= 1
                left += 1
        if right - left + 1 == k:
            ans += 1
        
        return ans

     

obj = Solution()
str, k = "heyfriendshowareyou", 5
ans = obj.KLenUniqueSubsequence(str, k)
print(ans)
        