class Solution:
    def moveZeroes(self, arr):
        zeroCount = 0

        for i in range(len(arr)):
            if arr[i] == 0:
                zeroCount += 1
            elif zeroCount > 0:
                temp = arr[i]
                arr[i] = 0
                arr[i-zeroCount] = temp
        
        return arr

obj = Solution()
arr = [0,1,0,3,12]
ans = obj.moveZeroes(arr)
print(ans)