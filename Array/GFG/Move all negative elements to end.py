class Solution:
    def moveNegativeElements(self, arr, n):
        temp, k = [0]*len(arr), 0

        for i in range(len(arr)):
            if arr[i] > -1 :
                temp[k] = arr[i]
                k += 1

        for i in range(len(arr)):
            if arr[i] < 0:
                temp[k] = arr[i]
                k += 1
               
        
        return temp

obj = Solution()
arr, n = [-5, 7, -3, -4, 9, 10, -1, 11], 8
ans = obj.moveNegativeElements(arr, n)
print(ans)