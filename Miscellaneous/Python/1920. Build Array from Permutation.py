class Solution:
    def buildArray(self, nums):
        result = [0]*len(nums)

        for i in range(len(nums)):
            result[i] = nums[nums[i]]
        
        return result


obj = Solution()
nums = [0,2,1,5,3,4]
ans = obj.buildArray(nums)
print(ans)