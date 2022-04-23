class Solution:
    def maxSubArraySum(self, arr):
        maxTillNow, maxEndingHere = 0, 0

        for i in range(len(arr)):
            maxEndingHere += arr[i]
            
            if maxTillNow < maxEndingHere:
                maxTillNow = maxEndingHere

            if maxEndingHere < 0:
                maxEndingHere = 0

        return maxTillNow

obj = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
ans = obj.maxSubArraySum(arr)
print(ans)