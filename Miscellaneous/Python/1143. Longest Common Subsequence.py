class Solution:
    def longestCommonSubsequence(self, text1, text2):
        dpArray = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    dpArray[row][col] = 1 + dpArray[row+1][col+1]
                else:
                    dpArray[row][col] = max(dpArray[row+1][col], dpArray[row][col+1])
        
        return dpArray[0][0]
    
    def longestCommonSubsequenceSpaceOptimized(self, text1, text2):
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        previous = [0 for i  in range(len(text1) + 1)]

        for col in reversed(range(len(text2))):

            current = [0 for i in range(len(text1) + 1)]
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row+1])

            previous = current
        
        return previous[0]


obj = Solution()
text1, text2 = "abcde",  "ace" 
ans = obj.longestCommonSubsequenceSpaceOptimized(text1, text2)
print(ans)
        