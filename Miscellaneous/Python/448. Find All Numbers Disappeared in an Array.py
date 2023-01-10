class Solution:
    def findDisappearedNumbers(self, nums):
        numsMap, result, i = {}, [], 1

        for num in nums:
            if num not in numsMap:
                numsMap[num] = 1
            else:
                numsMap[num] += 1
        
        while i <= len(nums):
            if i not in numsMap:
                result.append(i)
            i += 1
        
        return result


obj = Solution()
nums = [4,3,2,7,8,2,3,1]
ans = obj.findDisappearedNumbers(nums)
print(ans)