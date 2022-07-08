class Solution:
    def mergeArrays(self, arr1, n, arr2, m):
        for i in range(m):
            arr1.append(0)

        while m:
            if n and arr1[n - 1] >= arr2[m-1]:
                arr1[m+n-1] = arr1[n-1]
                n -= 1
            else:
                arr1[m+n-1] = arr2[m-1]
                m -= 1
        
        return arr1

obj = Solution()
arr1, arr2, n, m = [1, 3, 5, 7], [0, 2, 6, 8, 9], 4, 5
ans = obj.mergeArrays(arr1, n, arr2, m)
print(ans)