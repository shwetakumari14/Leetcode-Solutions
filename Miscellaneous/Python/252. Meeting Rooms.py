class Solution:
    def meetingRooms(self, intervals):
        intervals.sort()
        
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True

obj = Solution()
intervals = [[7,10],[2,4]]
ans = obj.meetingRooms(intervals)
print(ans)
        