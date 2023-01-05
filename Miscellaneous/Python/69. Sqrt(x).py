class Solution:
    def sqrt(self, x):
        if x == 0:
            return 0
        
        left, right = 1, x - 1

        while left < right - 1:
            mid = left + (right - left)//2
            if mid <= x//mid:
                left = mid
            else:
                right = mid - 1
        
        if right <= x // right:
            return right
        
        return left


obj = Solution()
ans = obj.sqrt(27)
print(ans)