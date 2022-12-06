class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans, n = [], len(nums)

        for i in range(n-1):
            l, r, x = i+1, n-1, nums[i]

            while l < r:
                if x + nums[l] + nums[r] == 0:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif x + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        
        return [list(x) for x in set(tuple(x) for x in ans)]


obj = Solution()
nums = [-1,0,1,2,-1,-4]
ans = obj.threeSum(nums)
print(ans)
        