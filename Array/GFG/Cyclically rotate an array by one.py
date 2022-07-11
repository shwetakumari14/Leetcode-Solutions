class Solution:
    def rotateArray(self, arr, n):
        if n == 1:
            return arr
        
        temp = arr[n-1]

        for i in range(n-1, -1, -1):
            arr[i] = arr[i-1]
        
        arr[0] = temp
        
        return arr

obj = Solution()
arr, n = [1, 2, 3, 4, 5],5
ans = obj.rotateArray(arr, n)
print(ans)