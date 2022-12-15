class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        numSum = 0

        for i in range(len(nums) - 2):
            numSum += self.twoSumSmaller(nums, i+1, target - nums[i])
        
        return numSum
    
    def twoSumSmaller(self, nums, startIdx, target):
        twoSum, left, right = 0, startIdx, len(nums)-1

        while left < right:
            if nums[left] + nums[right] < target:
                twoSum += right - left
                left += 1
            else:
                right -= 1
        
        return twoSum
     

obj = Solution()
nums, target = [-2, 0, 1, 3], 2
ans = obj.threeSumSmaller(nums, target)
print(ans)
        