class Solution:
    def isPerfectSquare(self, n):
        if n < 2:
            return False
        
        left, right = 2, n//2

        while left <= right:
            mid = left + (right - left)//2
            temp = mid * mid
            if temp == n:
                return True
            if temp > n:
                right = mid - 1
            else:
                left = mid + 1
        
        return False


obj = Solution()
n = 64
ans = obj.isPerfectSquare(n)
print(ans)