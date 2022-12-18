class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack, answers = [], [0]*n

        for currDay, currTemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currTemp:
                prevDay = stack.pop()
                answers[prevDay] = currDay - prevDay
            stack.append(currDay)

        return answers
     

obj = Solution()
temperatures = [73,74,75,71,69,72,76,73]
ans = obj.dailyTemperatures(temperatures)
print(ans)
        