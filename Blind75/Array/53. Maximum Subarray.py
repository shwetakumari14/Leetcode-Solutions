class Solution:
    def maxSubArray(self, nums):
        maxTillNow, maxEleHere = -1000000, 0
        
        for i in range(len(nums)):
            maxEleHere += nums[i]
            if maxTillNow < maxEleHere:
                maxTillNow = maxEleHere
            
            if maxEleHere < 0 :
                maxEleHere = 0
        
        return maxTillNow

obj = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
ans = obj.maxSubArray(arr)
print(ans)