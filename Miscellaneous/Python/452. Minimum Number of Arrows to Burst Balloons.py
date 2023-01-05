class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        points.sort(key = lambda x:x[1])

        arrows, first_end = 1, points[0][1]

        for x_start, x_end in points:
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        
        return arrows


obj = Solution()
points = [[1,2],[3,4],[5,6],[7,8]]
ans = obj.findMinArrowShots(points)
print(ans)