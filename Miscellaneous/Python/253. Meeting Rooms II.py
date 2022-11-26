import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        finalAns = []
        
        intervals.sort(key = lambda x:x[0])

        heapq.heappush(finalAns, intervals[0][1])

        for i in intervals[1:]:

            if finalAns[0] <= i[0]:
                heapq.heappop(finalAns)
            
            heapq.heappush(finalAns, i[1])
        
        return len(finalAns)

obj = Solution()
intervals = [[0,30],[5,10],[15,20]]
ans = obj.minMeetingRooms(intervals)
print(ans)
        