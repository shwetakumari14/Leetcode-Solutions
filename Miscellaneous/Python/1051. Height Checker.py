class Solution:
    def heightChecker(self, heights):
        expectedHeight, count = sorted(heights), 0

        for i in range(len(heights)):
            if expectedHeight[i] != heights[i]:
                count += 1
        
        return count

     

obj = Solution()
heights = [5,1,2,3,4]
ans = obj.heightChecker(heights)
print(ans)
        