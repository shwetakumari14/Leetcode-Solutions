class Solution:
    def tripletSum(self, A, n, X):
        count = 0

        for i in range(n):
            ans = set()
            currentSum = X - A[i]
            for j in range(i+1, n):
                if currentSum - A[j] in ans:
                    count += 1
                ans.add(A[j])

        
        return count

obj = Solution()
A, n , X = [1, 2, 3, 4, 6], 5, 10
ans = obj.tripletSum(A, n, X)
print(ans)