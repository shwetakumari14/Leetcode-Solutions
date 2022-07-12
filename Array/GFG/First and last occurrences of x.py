class Solution:
    def numOccurence(self, arr, n, x):
        ans, count = [], 0

        for i in range(n):
            if arr[i] == x:
                ans.append(i)
                count += 1

        if len(ans) == 0:
            return [-1, -1]
        
        return [ans[0], ans[count-1]]

obj = Solution()
arr, n, x = [1, 3, 5, 5, 5, 5, 67, 123, 125], 9, 5
ans = obj.numOccurence(arr, n, x)
print(ans)