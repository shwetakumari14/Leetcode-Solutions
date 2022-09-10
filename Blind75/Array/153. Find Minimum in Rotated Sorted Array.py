class Solution:
    def searchInRotatedSortedArray(self, arr):
        low, high = 0, len(arr) - 1

        while low < high:
            if arr[low] < arr[high]:
                return arr[low]
            
            mid = low + (high - low)//2
            if arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid

        
        return arr[low]
            
    
obj = Solution()
arr = [4,5,6,7,0,1,2]
ans = obj.searchInRotatedSortedArray(arr)
print(ans)