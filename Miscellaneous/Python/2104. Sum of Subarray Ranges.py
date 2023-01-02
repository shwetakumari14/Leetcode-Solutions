class Solution:
    def subArrayRanges(self, nums):
        n, result = len(nums), 0

        for left in range(n):
            maxVal, minVal = -float("inf"), float("inf")
            for right in range(left, n):
                maxVal = max(maxVal, nums[right])
                minVal = min(minVal, nums[right])
                result += maxVal - minVal
        
        return result

     

obj = Solution()
nums = [4,-2,-3,4,1]
ans = obj.subArrayRanges(nums)
print(ans)
        