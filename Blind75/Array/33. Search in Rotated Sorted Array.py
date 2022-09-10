class Solution:
    def searchInRotatedSortedArray(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1
            
    
obj = Solution()
arr, target = [4,5,6,7,0,1,2], 0
# arr, target = [5, 1, 3], 1
ans = obj.searchInRotatedSortedArray(arr, target)
print(ans)