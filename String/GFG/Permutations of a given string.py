def toString(arr):
    return "".join(arr)
            
class Solution:
    def permute(self, arr, l, r, temp):
        if l >= r:
            temp.add(toString(arr))
            return temp
        else:
            for i in range(l, r):
                arr[l], arr[i] = arr[i], arr[l]
                self.permute(arr, l+1, r, temp)
                arr[l], arr[i] = arr[i], arr[l]
            
    def find_permutation(self, S):
        l, r, arr, temp = 0, len(S), list(S) , set()

        self.permute(arr, l, r, temp)
        
        ans = sorted(list(temp))

        return ans

obj = Solution()
S = "ABC"
ans = obj.find_permutation(S)
print(ans)