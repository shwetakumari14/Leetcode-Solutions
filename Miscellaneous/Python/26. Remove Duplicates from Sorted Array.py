class Solution(object):
    def removeDuplicates(self, nums):
        dict = {}
        counter = 0

        for i in range(len(nums)):
           if nums[i] not in dict.keys():
               dict[nums[i]] = True
               counter += 1

    
        return counter

obj = Solution()
arr = [1,1,2]
ans = obj.removeDuplicates(arr)
print(ans)
