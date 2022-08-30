class Solution:
    def productExceptSelf(self, nums):
        prod, zeroCount = 1, 0
        
        for num in nums:
            if num == 0:
                zeroCount += 1
                continue
            if zeroCount < 2 :
                prod *= num
            else:
                prod = 0
                break
        
        for i in range(len(nums)):
            if zeroCount == 1 and nums[i] != 0:
                nums[i] = 0
            elif zeroCount == 1 and nums[i] == 0:
                nums[i] = prod
            elif zeroCount > 1:
                nums[i] = 0
            else:
                nums[i] = prod // nums[i]
        
        return nums
    
    def productExceptSelf2(self, nums):
        n, temp = len(nums), 1
        res = [1]*n

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            temp *= nums[i+1]
            res[i] *= temp        
        return res

obj = Solution()
arr = [1,2,3,4]
ans = obj.productExceptSelf2(arr)
print(ans)