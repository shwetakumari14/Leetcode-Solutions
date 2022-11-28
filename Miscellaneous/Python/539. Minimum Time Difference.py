class Solution:
    def convertToMin(self, time):
        time = time.split(":")
        minutes = (60*int(time[0])) + int(time[1])
        return minutes

    def findMinDifference(self, timePoints):
        for i, time in enumerate(timePoints):
            timePoints[i] = self.convertToMin(time)
        
        res = float("inf")
        timePoints.sort()

        for i in range(0, len(timePoints)-1):
            res = min(res, (timePoints[i+1] - timePoints[i]))
        
        res = min(res, (24*60-timePoints[-1] + timePoints[0]))

        return res

obj = Solution()
timePoints = ["23:59","00:00"]
ans = obj.findMinDifference(timePoints)
print(ans)
        