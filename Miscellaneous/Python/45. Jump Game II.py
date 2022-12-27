class Solution:
    def jump(self, nums):
        if len(nums) == 0:
            return 0
        
        if nums[0] == 0:
            return 0
        
        if len(nums) == 1 and nums[0] == 1:
            return 0
        
        jumps, maxReached, steps = 1, nums[0], nums[0]

        for i in range(1, len(nums)):
            if i == len(nums)-1:
                return jumps
            
            maxReached = max(maxReached, nums[i] + i)
            steps -= 1
            if steps == 0:
                jumps += 1
                if i >= maxReached:
                    return -1

                steps -= i
        
        return jumps



obj = Solution()
nums = [2,3,0,1,4]
ans = obj.jump(nums)
print(ans)