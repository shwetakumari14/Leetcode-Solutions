class Solution:
    def searchInRotatedSortedArray(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1



obj = Solution()
nums, target = [4,5,6,7,0,1,2], 0
ans = obj.searchInRotatedSortedArray(nums, target)
print(ans)
        