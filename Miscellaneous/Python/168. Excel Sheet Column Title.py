class Solution:
    def convertToTitle(self, columnNumber):
        result = ""

        while columnNumber > 0:
            result = chr((columnNumber - 1) % 26 + 65) + result
            columnNumber = (columnNumber - 1) // 26
        
        return result


obj = Solution()
columnNumber = 28
ans = obj.convertToTitle(columnNumber)
print(ans)