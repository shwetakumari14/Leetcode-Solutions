class Solution:
    def subsetArray(self, a1, a2, n, m):
        dict = {}

        for num in a2:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                
        for num in a1:
            if num in dict:
                dict[num] -= 1
                
        for num in dict.values():
            if num > 0:
                return "No"
        
        return "Yes"

obj = Solution()
a1, a2, n, m = [11, 1, 13, 21, 3, 7], [11, 3, 7, 1], 6, 4
ans = obj.subsetArray(a1, a2, n, m)
print(ans)