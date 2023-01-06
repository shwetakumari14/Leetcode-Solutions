class Solution:
    def wiggleSort(self, nums):

        for i in range(len(nums)-1):
            if (i % 2 == 0 and nums[i] > nums[i+1]) or (i % 2 == 1 and nums[i] < nums[i+1]) :
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
        return nums
        

obj = Solution()
nums = [3,5,2,1,6,4]
ans = obj.wiggleSort(nums)
print(ans)