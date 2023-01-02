class Solution:
    def findLonelyPixel(self, picture):
        row, col = len(picture), len(picture[0])
        result = 0

        for j in range(col):
            found = False
            for i in range(row):
                if picture[i][j] == "B":
                    if found or picture[i].count("B") != 1:
                        found = False
                        break
                    found = True
            if found:
                result += 1
        
        return result
        
     

obj = Solution()
picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
ans = obj.findLonelyPixel(picture)
print(ans)
        