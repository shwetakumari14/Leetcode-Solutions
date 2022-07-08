class Solution:
    def nextPermutation(self, arr, n):
        k = -1

        for i in range(len(arr)-1, -1, -1):
            if arr[i] > arr[i-1]:
                k = i - 1
                break
        
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > arr[k]:
                arr[i], arr[k] = arr[k], arr[i]
                break

        if k != -1:
            k += 1
            n = len(arr)-1

            while k < n:
                arr[k], arr[n] = arr[n], arr[k]
                k += 1
                n -= 1
            return arr
        else:
            arr.sort()
            return arr

obj = Solution()
arr, n = [3, 2, 1], 3
ans = obj.nextPermutation(arr, n)
print(ans)