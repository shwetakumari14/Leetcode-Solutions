class Solution:
    def reverseArray(self, arr):
        i, j = 0, len(arr)-1

        while i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        return arr

obj = Solution()
arr = [1, 2, 3, 4, 5]
ans = obj.reverseArray(arr)
print(ans)