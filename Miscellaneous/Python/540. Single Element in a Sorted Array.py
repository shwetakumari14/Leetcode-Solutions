class Solution:
    def singleNonDuplicate(self, nums):
        low, high = 0, len(nums)-1

        while low < high:
            mid = low + (high - low)//2
            isEvenHalf = (high - mid)%2 == 0
            if nums[mid] == nums[mid+1]:
                if isEvenHalf:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid-1]:
                if isEvenHalf:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        
        return nums[low]


obj = Solution()
nums = [1,1,2,3,3,4,4,8,8]
ans = obj.singleNonDuplicate(nums)
print(ans)
        