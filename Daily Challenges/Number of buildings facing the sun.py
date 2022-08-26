class Solution:
    def noOfBuilding(self, arr):
        max, count = arr[0], 1

        for i in range(1, len(arr)):
            if arr[i] < max:
                count += 1
                max = arr[i]
        
        return count

obj = Solution()
arr = [7, 4, 8, 2, 9]
ans = obj.noOfBuilding(arr)
print(ans)