from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        if not points:
            return 0
        
        def findSlope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            if x1 - x2 == 0:
                return float("inf")
            
            return (y1 - y2) / (x1 - x2)
        
        result = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for j, p2 in enumerate(points[i+1:]):
                slope = findSlope(p1, p2)
                slopes[slope] += 1
                result = max(result, slopes[slope])
        
        return result + 1


obj = Solution()
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
ans = obj.maxPoints(points)
print(ans)