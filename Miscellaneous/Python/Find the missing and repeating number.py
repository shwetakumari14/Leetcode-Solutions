class Solution:
    def findDuplicate(self, nums):
        duplicate, repeating = -1, -1
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
            else:
                duplicate = abs(nums[i])
                break
        
        for i in range(len(nums)):
            if nums[i] > 0:
                repeating = i + 1
                break
        
        return [duplicate, repeating]
     

obj = Solution()
nums = [4, 3, 6, 2, 1, 1]
ans = obj.findDuplicate(nums)
print(ans)
        