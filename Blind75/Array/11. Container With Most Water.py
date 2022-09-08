class Solution:
    def maxArea(sefl, height):
        n, ans = len(height), 0
        left, right, width = 0, n-1, n-1

        for i in range(width, 0, -1):
            if height[left] < height[right]:
                ans = max(ans, height[left] * i)
                left += 1
            else:
                ans = max(ans, height[right] * i)
                right -= 1

        return ans

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
ans = obj.maxArea(height)
print(ans)