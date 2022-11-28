from math import ceil

class Solution:
    def minimizeArrayValue(self, nums):
        result, currSum = 0, 0

        for i, num in enumerate(nums, start=1):
            currSum += num
            result = max(result, ceil(currSum/i))
        
        return result
            


obj = Solution()
nums = [3,7,1,6]
ans = obj.minimizeArrayValue(nums)
print(ans)
        