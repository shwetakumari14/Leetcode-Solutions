class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [0]*n
        answer[0] = 1

        for i in range(1, n):
            answer[i] = answer[i-1]*nums[i-1]
        
        rightProd = 1

        for i in reversed(range(n)):
            answer[i] *= rightProd
            rightProd *= nums[i]
        
        return answer

obj = Solution()
nums = [-1,1,0,-3,3]
ans = obj.productExceptSelf(nums)
print(ans)
        