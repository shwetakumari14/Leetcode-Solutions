class Solution:
    def missingRanges(self, arr, lower, higher):
        ans, low, up, overFlow = [], lower, higher, False

        for i in range(len(arr)):
            if low < arr[i]:
                ans.append(self.getRange(low, arr[i]-1))
            
            low = arr[i]+1
            if low == -1000000:
                overFlow = True
                break
        
        if low <=up and not overFlow:
            ans.append(self.getRange(low, up))

        return ans

    def getRange(self, a, b):
        if a == b:
            return str(a)
        else:
            return str(a) + "->" + str(b)

obj = Solution()
arr, lower, higher = [0, 1, 3, 50, 75], 0, 99
ans = obj.missingRanges(arr, lower, higher)
print(ans)