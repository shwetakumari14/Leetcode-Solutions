class Solution:
    def numIdenticalPairs(self, nums):
        result = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    result += 1
        
        return result

obj = Solution()
nums = [1,2,3,1,1,3]
ans = obj.numIdenticalPairs(nums)
print(ans)