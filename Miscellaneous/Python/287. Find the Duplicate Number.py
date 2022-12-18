class Solution:
    def findDuplicate(self, nums):
        duplicate = -1

        for num in nums:
            curr = abs(num)
            if nums[curr] < 0:
                duplicate = curr
                break
            nums[curr] = -nums[curr]
        

        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        
        return duplicate
     

obj = Solution()
nums = [1,3,4,2,2]
ans = obj.findDuplicate(nums)
print(ans)
        