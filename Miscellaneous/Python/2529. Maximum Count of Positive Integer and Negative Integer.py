class Solution:
    def maximumCount(self, nums):
        pos, neg = 0, 0

        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        
        return max(pos, neg)



obj = Solution()
nums = [-2,-1,-1,1,2,3]
ans = obj.maximumCount(nums)
print(ans)