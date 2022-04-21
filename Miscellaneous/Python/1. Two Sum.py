nums = [3,2,4]
target = 6

class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                   result.append(i)
                   result.append(j)
                return result

    def twoSum2(self, nums, target):
        tempMap = {}
        for i in range(len(nums)):
            if target - nums[i] in tempMap:
                return [tempMap[target-nums[i]], i]
            else:
                tempMap[nums[i]]=i


x = Solution()
print(x.twoSum2(nums, target))
        