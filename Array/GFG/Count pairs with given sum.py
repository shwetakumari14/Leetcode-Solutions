class Solution:
    def sumPair(self, arr, n):
        dict, count = {}, 0
        
        for i in range(n):
            if k - arr[i] in dict:
                count += dict[k - arr[i]]
            if arr[i] in dict:
                dict[arr[i]] += 1
            else:
                dict[arr[i]] = 1
               
        
        return count

obj = Solution()
arr, n, k = [1, 1, 1, 1], 4, 2
ans = obj.sumPair(arr, n)
print(ans)