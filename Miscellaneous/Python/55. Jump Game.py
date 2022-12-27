class Solution:
    def canJump(self, nums):
        length = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= length:
                length = i
        
        return length == 0


obj = Solution()
nums = [2,3,1,1,4]
ans = obj.canJump(nums)
print(ans)