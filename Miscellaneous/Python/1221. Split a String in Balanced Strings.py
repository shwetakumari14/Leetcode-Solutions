class Solution:
    def balancedStringSplit(self, s):
        charCount, result = 0, 0

        for char in s:
            if char == "L":
                charCount += 1
            else:
                charCount -= 1
            if charCount == 0:
                result += 1
        
        return result


obj = Solution()
s = "RLRRLLRLRL"
ans = obj.balancedStringSplit(s)
print(ans)