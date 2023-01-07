class Solution:
    def pivotArray(self, nums, pivot):
        left, right = [], []

        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
        
        for num in nums:
            if num == pivot:
                left.append(num)
        
        return left + right



obj = Solution()
nums, pivot = [9,12,5,10,14,3,10], 10
ans = obj.pivotArray(nums, pivot)
print(ans)