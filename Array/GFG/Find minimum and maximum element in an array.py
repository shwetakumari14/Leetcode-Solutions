class Solution:
    def minMaxElement(self, arr):
        min, max = arr[0], arr[0]

        for i in range(1, len(arr)):
            if arr[i] > max:
                max = arr[i]
            if arr[i] < min:
                min = arr[i]

        return min, max

obj = Solution()
arr = [1, 345, 234, 21, 56789]
min, max = obj.minMaxElement(arr)
print(min, max)