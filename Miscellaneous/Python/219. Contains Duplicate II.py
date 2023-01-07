class Solution:
    def containsNearbyDuplicate(self, nums, k):
        numDict = {}

        for i, j in enumerate(nums):
            if j in numDict and i - numDict[j] <= k:
                return True
            numDict[j] = i
        
        return False


obj = Solution()
nums, k = [1,2,3,1], 3
ans = obj.containsNearbyDuplicate(nums, k)
print(ans)