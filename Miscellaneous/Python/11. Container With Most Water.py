class Solution:
    def maxArea(self, height):
        left, right, maxArea = 0, len(height)-1, 0

        while left < right:
            width = right - left
            maxArea = max(maxArea, min(height[left], height[right])*width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea



obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
ans = obj.maxArea(height)
print(ans)
        