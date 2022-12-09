class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) == 0:
            return 0
        
        end, count = float("-inf"), 0

        for s, e in sorted(intervals, key = lambda x:x[1]):
            if s >= end:
                end = e
            else:
                count += 1
        
        return count

obj = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
ans = obj.eraseOverlapIntervals(intervals)
print(ans)
        