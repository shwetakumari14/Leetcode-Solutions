class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        difference = float("inf")
        for i in range(len(nums)):
            low, high = i + 1, len(nums)-1

            while low < high:
                tempSum = nums[low] + nums[high] + nums[i]
                if abs(target - tempSum) < abs(difference):
                    difference = target - tempSum
                if tempSum < target:
                    low += 1
                else:
                    high -= 1
        
        return target - difference

obj = Solution()
nums, target = [-1, 2, 1, -4], 1
ans = obj.threeSumClosest(nums, target)
print(ans)
        