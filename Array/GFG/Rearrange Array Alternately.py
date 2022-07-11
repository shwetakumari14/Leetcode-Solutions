class Solution:
    def arrayUnion(self, arr, n):
        maxIdx, minIdx, maxEle = n-1, 0, arr[n-1]+1

        for i in range(n):
            if i%2 == 0:
                arr[i] += (arr[maxIdx] % maxEle) * maxEle
                maxIdx -= 1
            else:
                arr[i] += (arr[minIdx] % maxEle) * maxEle
                minIdx += 1

        for i in range(n):
            arr[i] =  arr[i] // maxEle    

        
        return arr

obj = Solution()
arr, n = [1,2,3,4,5,6], 6
ans = obj.arrayUnion(arr, n)
print(ans)