class Solution:
    def nextPermutation(self, nums):
        breakpoint = -1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[i-1]:
                breakpoint = i-1
                break
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[breakpoint]:
                nums[i], nums[breakpoint] = nums[breakpoint], nums[i]
                break

        if breakpoint > -1 :
            breakpoint += 1
            n = len(nums)-1
            while breakpoint < n:
                nums[breakpoint], nums[n] = nums[n], nums[breakpoint]
                n -= 1
                breakpoint += 1

            return nums
        
        nums.sort()
        return nums

obj = Solution()
nums = [1,2,3]
ans = obj.nextPermutation(nums)
print(ans)
        