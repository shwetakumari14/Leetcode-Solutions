class Solution:
    def missingNum(self, arr):
        sum, n = 0, len(arr)
        sum = (n * (n+1)) // 2

        for num in arr:
            sum -= num
        
        return sum

obj = Solution()
arr = [9,6,4,2,3,5,7,0,1]
ans = obj.missingNum(arr)
print(ans)