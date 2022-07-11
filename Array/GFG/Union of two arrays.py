class Solution:
    def arrayUnion(self, arr1, arr2, n, m):
        ans = set()

        for i in range(n):
            ans.add(arr1[i])

        for i in range(m):
            ans.add(arr2[i])

        
        return len(ans)

obj = Solution()
arr1, arr2, n, m = [1, 2, 3, 4, 5], [1, 2, 3], 5, 3
ans = obj.arrayUnion(arr1, arr2, n, m)
print(ans)