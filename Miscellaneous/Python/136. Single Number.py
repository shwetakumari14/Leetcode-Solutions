class Solution:
    def singleNumber(self, nums):
        ans = nums[0]

        for i in range(1, len(nums)):
            ans = ans ^ nums[i]

        return ans

obj = Solution()
arr = [2,2,1]
ans = obj.singleNumber(arr)
print(ans)