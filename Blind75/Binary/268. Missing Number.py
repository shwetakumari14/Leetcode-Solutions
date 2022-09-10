class Solution:
    def reverseBits(self, arr):
        n = len(arr)
        sumOfArr = n * (n+1) // 2

        for i in range(n):
            sumOfArr -= arr[i]
        
        return sumOfArr



obj = Solution()
arr = [9,6,4,2,3,5,7,0,1]
ans = obj.reverseBits(arr)
print(ans)