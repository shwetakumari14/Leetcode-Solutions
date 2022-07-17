class Solution:
    def heapify(self, arr, n, i):
        largest = i
        left, right = 2*i + 1, 2*i + 2

        if left < n and arr[largest] < arr[left]:
            largest = left
        
        if right < n and arr[largest] < arr[right]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def heapSort(self, arr, n):
        
        for i in range(n//2-1, -1, -1):
            self.heapify(arr, n, i)
        
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0) 

        return arr

obj = Solution()
arr, n = [12, 11, 13, 5, 6, 7], 6
ans = obj.heapSort(arr, n)
print(ans)