class Solution:
    def mergeArrays2(self, arr1, n, arr2, m):
        i, j = n-1, 0

        while i >=0 and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]

            i -= 1
            j += 1
        
        arr1.sort()
        arr2.sort()
        
        return arr1, arr2

obj = Solution()
arr1, arr2, n, m = [1, 3, 5, 7], [0, 2, 6, 8, 9], 4, 5
ans1, ans2 = obj.mergeArrays2(arr1, n, arr2, m)
print(ans1, ans2)