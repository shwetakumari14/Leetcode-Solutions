class Solution:
    def containsDuplicate(self, nums):
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
        
        return False

obj = Solution()
arr = [1,1,1,3,3,4,3,2,4,2]
ans = obj.containsDuplicate(arr)
print(ans)