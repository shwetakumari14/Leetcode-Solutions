class Solution:
    def robHouse(self, nums):
        if not nums:
            return 0

        n = len(nums)
        robNext, robNextPlusOne = nums[n-1], 0

        for i in range(n-2, -1, -1):

            current = max(robNext, robNextPlusOne + nums[i])
            robNextPlusOne = robNext
            robNext = current
        
        return robNext

obj = Solution()
nums = [2,7,9,3,1]
ans = obj.robHouse(nums)
print(ans)
        