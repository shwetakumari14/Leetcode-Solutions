class Solution:
    def sort012(self, arr, n):
        low, high, mid = 0, n-1, 0

        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr

obj = Solution()
arr, n = [0, 2, 1, 2, 0], 5
ans = obj.sort012(arr, n)
print(ans)