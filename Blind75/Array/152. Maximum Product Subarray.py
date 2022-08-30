class Solution:
    def maxProduct(self, nums):
        maxProd, minProd, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            x = max(nums[i], maxProd*nums[i], minProd*nums[i])
            y = min(nums[i], maxProd*nums[i], minProd*nums[i])
            maxProd, minProd = x , y
            ans = max(ans, maxProd)
        
        return ans

obj = Solution()
arr = [2,3,-2,4]
ans = obj.maxProduct(arr)
print(ans)