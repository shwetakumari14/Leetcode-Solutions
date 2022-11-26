class Solution:
    def mergeIntervals(self, intervals):
        merged = []

        intervals.sort(key = lambda x:x[0])

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            
            merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

obj = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = obj.mergeIntervals(intervals)
print(ans)
        