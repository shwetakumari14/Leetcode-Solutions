class Solution:
    def trapWater(self, height):
        n, res = len(height), 0
        left, right = [0]*n, [0]*n
        left[0], right[n-1] = height[0], height[n-1]

        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        for i in range(n-2, 0, -1):
            right[i] = max(right[i+1], height[i])
        
        for i in range(1, n):
            res += min(left[i], right[i]) - height[i]
        
        return res



obj = Solution()
height = [4,2,0,3,2,5]
ans = obj.trapWater(height)
print(ans)
        