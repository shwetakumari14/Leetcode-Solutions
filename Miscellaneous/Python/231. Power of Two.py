class Solution:
    def isPowerOfTwo(self, num):
        if num == 0:
            return False
        
        return num & (-num) == num


obj = Solution()
num = 64
ans = obj.isPowerOfTwo(num)
print(ans)