class Solution:
    def findMin(self, arr):
        if len(arr) == 1:
            return arr[0]
        
        left, right = 0, len(arr)-1

        if arr[right] > arr[0]:
            return arr[0]
        
        if left <= right:
            mid = left + (right - left)//2

            if arr[mid] > arr[mid+1]:
                return arr[mid+1]
            if arr[mid-1] > arr[mid]:
                return arr[mid]
            
            if arr[mid] > arr[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

obj = Solution()
arr = [4,5,6,7,0,1,2]
ans = obj.findMin(arr)
print(ans)
        