class Solution:
    def kadanesAlgorithm (self, arr, n):
        maxTillNow, maxEndingHere = -10000000, 0

        for i in range(n):
            maxEndingHere += arr[i]
            if maxTillNow < maxEndingHere:
                maxTillNow = maxEndingHere
                
            if maxEndingHere < 0:
                maxEndingHere = 0

        return maxTillNow

obj = Solution()
arr, n = [-1,-2,-3,-4], 4
ans = obj.kadanesAlgorithm(arr, n)
print(ans)