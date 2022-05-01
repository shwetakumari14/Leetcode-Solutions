from re import I


class Solution:
   def majorityElement(self, arr):
        res, times = 0, 0

        for num in arr:
            if times == 0:
                res = num
            elif res == num:
                times += 1
            else:
                times -= 1
        
        return res

obj = Solution()
arr = [2,2,1,1,1,2,2]
ans = obj.majorityElement(arr)
print(ans)