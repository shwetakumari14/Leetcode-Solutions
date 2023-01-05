class Solution:
    def generatePossibleNextMoves(self, currentState):
        result = []

        for i in range(len(currentState)-1):
            if currentState[i:i+2] == "++":
                result.append(currentState[:i] + "--" + currentState[i+2:])
        
        return result


obj = Solution()
currentState = "++++"
ans = obj.generatePossibleNextMoves(currentState)
print(ans)