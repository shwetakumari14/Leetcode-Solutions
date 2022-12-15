class Solution:
    def majorityElementTwo(self, nums):
        if not nums:
            return []
        
        count1, count2, candidate1, candidate2 = 0, 0, None, None

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
            
        result = []
        
        for num in [candidate1, candidate2]:
            if nums.count(num) > len(nums)//3:
                result.append(num)
        
        return result

     

obj = Solution()
nums = [3,2,3]
ans = obj.majorityElementTwo(nums)
print(ans)
        