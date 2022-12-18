class Solution:
    def lis(self, arr, n):
        result = 0
        lis = [1 for i in range(n)]

        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j] and lis[i] < lis[j]+1:
                    lis[i] = lis[j] + 1
        
        for i in range(n):
            if result < lis[i]:
                result = lis[i]
        
        return result


    def minimumNumberOfDeletions(self, nums):
        length = self.lis(nums, len(nums))
        return len(nums) - length
     

obj = Solution()
nums = [30, 40, 2, 5, 1, 7, 45, 50, 8]
ans = obj.minimumNumberOfDeletions(nums)
print(ans)
        