class Solution:
    def countPairs(self, nums, k):
        count = 0

        for i in range(len(nums)):
            for j in range(i):
                if i != j:
                    if nums[i] == nums[j] and (i*j) % k == 0:
                        count += 1

        
        return count

     

obj = Solution()
nums, k = [3,1,2,2,2,1,3], 2
ans = obj.countPairs(nums, k)
print(ans)
        