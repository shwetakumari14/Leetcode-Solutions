class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dpArray = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dpArray[i] = max(dpArray[i], dpArray[j]+1)
        
        return max(dpArray)

     

obj = Solution()
nums = [10,9,2,5,3,7,101,18]
ans = obj.lengthOfLIS(nums)
print(ans)
        