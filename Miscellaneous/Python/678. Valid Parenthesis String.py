class Solution:
    def checkValidString(self, str):
        low, high = 0, 0

        for char in str:
            low += 1 if char == "(" else -1
            high += 1 if char != ")" else - 1
            if high < 0:
                break
            low = max(0, low)
        
        return low == 0



obj = Solution()
str = "(*))"
ans = obj.checkValidString(str)
print(ans)
        