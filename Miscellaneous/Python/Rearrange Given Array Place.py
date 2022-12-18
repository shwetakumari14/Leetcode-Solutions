class Solution:
    def rearrange(self, arr, n):
        
        for i in range(n):
            arr[i] += (arr[arr[i]] % n) * n
        
        for i in range(n):
            arr[i] = arr[i] // n
        
        return arr

     

obj = Solution()
nums = [3, 2, 0, 1]
ans = obj.rearrange(nums, len(nums))
print(ans)
        