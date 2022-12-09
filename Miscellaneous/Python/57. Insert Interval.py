class Solution:
    def insertInterval(self, intervals, newInterval):
        startNew, endNew = newInterval
        idx, n, result = 0, len(intervals), []

        while idx < n and startNew > intervals[idx][0]:
            result.append(intervals[idx])
            idx += 1
        
        if not result or result[-1][1] < startNew:
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], endNew)
        
        while idx < n:
            start, end = intervals[idx]

            if result[-1][1] < start:
                result.append(intervals[idx])
            else:
                result[-1][1] = max(result[-1][1], end)

            idx += 1
        
        return result

obj = Solution()
intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
ans = obj.insertInterval(intervals, newInterval)
print(ans)
        